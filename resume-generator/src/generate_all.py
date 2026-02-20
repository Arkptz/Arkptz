#!/usr/bin/env python3
"""Generate all resume variants, README, and portfolio."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_backend import generate as gen_backend
from generate_ml import generate as gen_ml
from generate_quant import generate as gen_quant
from generate_readme import generate as gen_readme

# Import portfolio generator
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "portfolio-generator" / "src"))
from generate_portfolio import generate as gen_portfolio


def main():
    root_dir = Path(__file__).parent.parent.parent
    output_dir = root_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Generate resumes
    gen_backend(str(output_dir / "Arkadiy_Pechnikov_Resume_Backend.pdf"))
    gen_ml(str(output_dir / "Arkadiy_Pechnikov_Resume_ML.pdf"))
    gen_quant(str(output_dir / "Arkadiy_Pechnikov_Resume_Quant.pdf"))
    
    # Generate README
    gen_readme(str(output_dir / "README.md"))
    
    # Generate portfolio
    gen_portfolio(str(output_dir / "portfolio"))

    print(f"\nAll files generated in {output_dir}/")
    print(f"Portfolio ready for GitHub Pages: {output_dir}/portfolio/index.html")


if __name__ == "__main__":
    main()
