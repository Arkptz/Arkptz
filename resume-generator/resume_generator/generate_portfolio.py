#!/usr/bin/env python3
"""Generate portfolio website from data.json for GitHub Pages.

Architecture:
  - output/portfolio/index.html  — static terminal-style portfolio
  - output/portfolio/data.js     — auto-generated JS wrapper around data.json
  - data.json is the single source of truth for ALL content

data.js is simply: window.PORTFOLIO_DATA = <contents of data.json>;
This avoids CORS issues when opening index.html from file:// protocol.
"""

import json
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent
DATA_PATH = ROOT_DIR / "data.json"
OUTPUT_DIR = ROOT_DIR / "output" / "portfolio"


def validate_data(data: dict) -> list[str]:
    errors = []
    required = ["personal", "meta", "skills", "experience", "education"]
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    if "personal" in data:
        for f in ["name", "email", "github"]:
            if f not in data["personal"]:
                errors.append(f"Missing personal.{f}")
    return errors


def generate(output_dir: str = None):
    """Generate data.js from data.json for the portfolio."""
    if output_dir is None:
        output_dir = OUTPUT_DIR

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load and validate
    with open(DATA_PATH, encoding="utf-8") as f:
        data = json.load(f)

    errors = validate_data(data)
    if errors:
        print("⚠ Validation warnings:")
        for e in errors:
            print(f"  - {e}")

    # Generate data.js (JS wrapper around JSON)
    data_js = output_path / "data.js"
    with open(data_js, "w", encoding="utf-8") as f:
        f.write("// Auto-generated from data.json — do not edit directly\n")
        f.write("window.PORTFOLIO_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"✓ Generated data.js → {data_js}")

    # Verify index.html exists
    index = output_path / "index.html"
    if index.exists():
        print(f"✓ index.html exists at {index}")
    else:
        print(f"⚠ index.html not found at {index}")

    print(f"✓ Portfolio ready: {output_path}")
    return str(output_path)


if __name__ == "__main__":
    generate()
