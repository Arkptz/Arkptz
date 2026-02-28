#!/usr/bin/env python3
"""Generate all resume variants, README, and portfolio."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from generate_backend import generate as gen_backend
from generate_ml import generate as gen_ml
from generate_techlead import generate as gen_techlead
from generate_readme import generate as gen_readme
from generate_portfolio import generate as gen_portfolio


def main():
    root_dir = Path(__file__).parent.parent.parent
    output_dir = root_dir / "output"
    output_dir.mkdir(exist_ok=True)

    gen_backend(str(output_dir / "Arkadiy_Pechnikov_Resume_Backend.pdf"))
    gen_ml(str(output_dir / "Arkadiy_Pechnikov_Resume_ML.pdf"))
    gen_techlead(str(output_dir / "Arkadiy_Pechnikov_Resume_TechLead.pdf"))
    gen_readme(str(root_dir / "README.md"))
    gen_portfolio(str(output_dir / "portfolio"))

    print(f"\nAll files generated in {output_dir}/")


if __name__ == "__main__":
    main()
