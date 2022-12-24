#!/usr/bin/env python3
"""Generate all resume variants, README, portfolio, and LinkedIn texts."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from .generate_backend_crypto import generate as gen_backend_crypto
from .generate_backend_traditional import generate as gen_backend_traditional
from .generate_techlead_crypto import generate as gen_techlead_crypto
from .generate_techlead_traditional import generate as gen_techlead_traditional
from .generate_cto import generate as gen_cto
from .generate_readme import generate as gen_readme
from .generate_portfolio import generate as gen_portfolio
from .generate_linkedin import generate as gen_linkedin


def main():
    root_dir = Path(__file__).parent.parent.parent
    output_dir = root_dir / "output"
    output_dir.mkdir(exist_ok=True)

    gen_backend_crypto(str(output_dir / "Arkadiy_Pechnikov_Resume_Backend_Crypto.pdf"))
    gen_backend_traditional(str(output_dir / "Arkadiy_Pechnikov_Resume_Backend.pdf"))
    gen_techlead_crypto(str(output_dir / "Arkadiy_Pechnikov_Resume_TechLead_Crypto.pdf"))
    gen_techlead_traditional(str(output_dir / "Arkadiy_Pechnikov_Resume_TechLead.pdf"))
    gen_cto(str(output_dir / "Arkadiy_Pechnikov_Resume_CTO.pdf"))
    gen_readme(str(root_dir / "README.md"))
    gen_portfolio(str(output_dir / "portfolio"))
    gen_linkedin(str(output_dir / "linkedin_texts.md"))

    print(f"\nAll files generated in {output_dir}/")


if __name__ == "__main__":
    main()
