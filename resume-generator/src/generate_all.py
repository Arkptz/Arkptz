#!/usr/bin/env python3
"""Generate all resume variants and README."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_backend import generate as gen_backend
from generate_ml import generate as gen_ml
from generate_quant import generate as gen_quant
from generate_readme import generate as gen_readme


def main():
    output_dir = Path(__file__).parent.parent.parent / "output"
    output_dir.mkdir(exist_ok=True)

    gen_backend(str(output_dir / "Arkadiy_Pechnikov_Resume_Backend.pdf"))
    gen_ml(str(output_dir / "Arkadiy_Pechnikov_Resume_ML.pdf"))
    gen_quant(str(output_dir / "Arkadiy_Pechnikov_Resume_Quant.pdf"))
    gen_readme(str(output_dir / "README.md"))

    print(f"\nAll files generated in {output_dir}/")


if __name__ == "__main__":
    main()
