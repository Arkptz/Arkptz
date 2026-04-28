{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/4aa36568d413aca0ea84a1684d2d46f55dbabad7";

    flake-parts.url = "github:hercules-ci/flake-parts";

    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix-hammer-overrides = {
      url = "github:TyberiusPrime/uv2nix_hammer_overrides";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    git-hooks-nix = {
      url = "github:cachix/git-hooks.nix";
    };
  };

  outputs =
    inputs@{
      nixpkgs,
      flake-parts,
      uv2nix,
      pyproject-nix,
      pyproject-build-systems,
      uv2nix-hammer-overrides,
      ...
    }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      imports = [
        inputs.git-hooks-nix.flakeModule
      ];

      systems = [
        "x86_64-linux"
        "aarch64-darwin"
        "x86_64-darwin"
      ];

      perSystem =
        {
          config,
          self',
          inputs',
          pkgs,
          system,
          lib,
          ...
        }:
        {
          pre-commit.pkgs = import inputs.git-hooks-nix.inputs.nixpkgs { inherit system; };
          pre-commit.settings.hooks = {
            djlint-lint = {
              enable = true;
              name = "djlint-lint";
              entry = "${pkgs.djlint}/bin/djlint --profile jinja --lint --ignore H006,H021,H023,H031";
              files = "\\.html\\.j2$";
              types = [ "file" ];
            };
            djlint-format = {
              enable = true;
              name = "djlint-format";
              entry = "${pkgs.djlint}/bin/djlint --profile jinja --reformat --format-css --quiet";
              files = "\\.html\\.j2$";
              types = [ "file" ];
            };
            nixfmt-rfc-style.enable = true;
            ruff-format.enable = true;
            ruff.enable = true;
          };

          devShells.default =
            let
              pkgs = import nixpkgs {
                inherit system;
              };
              workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
              overlay = workspace.mkPyprojectOverlay {
                sourcePreference = "wheel";
              };
              python = pkgs.python311;
              pythonPackages = python.pkgs;
              pyprojectOverrides = uv2nix-hammer-overrides.overrides_strict pkgs;
              editableOverlay = workspace.mkEditablePyprojectOverlay {
                # Use environment variable
                root = "$REPO_ROOT/resume-generator";
              };
              pythonSet =
                # Use base package set from pyproject.nix builders
                (pkgs.callPackage pyproject-nix.build.packages {
                  inherit python;
                }).overrideScope
                  (
                    lib.composeManyExtensions [
                      pyproject-build-systems.overlays.default
                      overlay
                      pyprojectOverrides
                    ]
                  );

              editablePythonSet = pythonSet.overrideScope editableOverlay;
              makeLibraryPath =
                packages: pkgs.lib.concatStringsSep ":" (map (package: "${pkgs.lib.getLib package}/lib") packages);
              libs = with pkgs; [
                openssl
                stdenv.cc.cc.lib
              ];
              virtualenv = editablePythonSet.mkVirtualEnv "arkptz-dev-env" workspace.deps.all;
            in
            pkgs.mkShell {
              NIX_LD_LIBRARY_PATH = makeLibraryPath libs;

              packages = [
                pkgs.nixfmt-rfc-style
                virtualenv
                pkgs.uv
                pkgs.mdformat
                pkgs.djlint
                pkgs.poetry
                pkgs.git
                pkgs.htop
                pkgs.tree
                pythonPackages.pylance
                pythonPackages.pylint
                pythonPackages.ruff
              ]
              ++ config.pre-commit.settings.enabledPackages;

              shellHook = ''
                ${config.pre-commit.installationScript}
                unset SOURCE_DATE_EPOCH
                unset PYTHONPATH


                # Get repository root using git. This is expanded at runtime by the editable `.pth` machinery.
                export REPO_ROOT=$(git rev-parse --show-toplevel)


                # Performance optimizations
                export PYTHONUNBUFFERED=1
                export PYTHONDONTWRITEBYTECODE=1

                # Cache directories for better performance
                export RUFF_CACHE_DIR="$REPO_ROOT/.ruff_cache"
                export MYPY_CACHE_DIR="$REPO_ROOT/.mypy_cache"
                export PYLINT_CACHE_DIR="$REPO_ROOT/.pylint_cache"


                # Stop uv from syncing
                export UV_NO_SYNC=1
                export UV_PYTHON=$(which python)
                # Stop uv from downloading python
                export UV_PYTHON_DOWNLOADS=never
                rm -rf ./.venv 2>/dev/null; ln -sfT ${virtualenv.out} ./.venv

              '';
            };
        };
    };
}
