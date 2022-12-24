#!/usr/bin/env python3
"""Generate portfolio website from data.json via Jinja2 template.

Architecture:
  - resume-generator/templates/portfolio.html.j2 - Jinja2 template
  - output/portfolio/index.html                  - rendered static HTML
  - data.json is the single source of truth for ALL content
"""

import json
import re
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent
DATA_PATH = ROOT_DIR / "data.json"
TEMPLATES_DIR = SCRIPT_DIR.parent / "templates"
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


def generate(output_dir: str = ""):
    if not output_dir:
        output_path = OUTPUT_DIR
    else:
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

    # Set up Jinja2
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        keep_trailing_newline=True,
    )
    env.filters["tojson"] = lambda v, indent=None: json.dumps(v, indent=indent, ensure_ascii=False)

    # Render template
    template = env.get_template("portfolio.html.j2")
    html = template.render(data=data)

    # Write index.html
    index = output_path / "index.html"
    index.write_text(html, encoding="utf-8")
    print(f"✓ Rendered portfolio → {index}")

    # Update sitemap.xml lastmod
    sitemap = output_path / "sitemap.xml"
    if sitemap.exists():
        today = date.today().isoformat()
        sitemap_content = sitemap.read_text(encoding="utf-8")
        if "<lastmod>" in sitemap_content:
            sitemap_content = re.sub(
                r"<lastmod>[^<]+</lastmod>",
                f"<lastmod>{today}</lastmod>",
                sitemap_content,
            )
        else:
            sitemap_content = sitemap_content.replace(
                "<changefreq>",
                f"<lastmod>{today}</lastmod>\n    <changefreq>",
            )
        sitemap.write_text(sitemap_content, encoding="utf-8")
        print(f"✓ Updated sitemap.xml lastmod → {today}")

    print(f"✓ Portfolio ready: {output_path}")
    return str(output_path)


if __name__ == "__main__":
    generate()
