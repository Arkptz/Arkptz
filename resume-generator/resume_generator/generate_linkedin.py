#!/usr/bin/env python3
"""Generate LinkedIn profile texts from data.json - fully data-driven."""

from pathlib import Path

from .shared import load_data


def _format_experience(data: dict) -> str:
    """Compose experience descriptions from data.json experience entries."""
    sections = []
    title_variant = "crypto_lead"

    for job in data["experience"]:
        title = job.get("titles", {}).get(title_variant, "")
        company = job.get("company", "")
        period = job.get("period", "")
        product = job.get("product", "")

        header = f"### {company} | {title} | {period}"

        intro = product if product else ""

        bullets = job.get("bullets", [])[:5]
        bullet_texts = [b["text"] for b in bullets if b.get("text")]
        bullet_list = "\n".join(f"→ {t}" for t in bullet_texts)

        # Tech stack
        tech = job.get("tech", [])
        if isinstance(tech, dict):
            tech_list = tech.get("crypto", [])
        else:
            tech_list = tech
        tech_line = f"**Tech:** {', '.join(tech_list)}" if tech_list else ""

        # LinkedIn skills for this position
        li_skills = job.get("linkedin_skills", [])
        skills_line = f"**LinkedIn Skills:** {', '.join(li_skills)}" if li_skills else ""

        parts = [header, ""]
        if intro:
            parts.append(intro)
            parts.append("")
        parts.append(bullet_list)
        if tech_line:
            parts.append("")
            parts.append(tech_line)
        if skills_line:
            parts.append(skills_line)

        sections.append("\n".join(parts))

    return "\n\n".join(sections)


def _format_skills(data: dict) -> str:
    lines = []
    skip_categories = {"leadership", "soft_skills"}
    for key, category in data["skills"].items():
        if key in skip_categories:
            continue
        if isinstance(category, dict) and "items" in category:
            label = category.get("label", key.title())
            items = ", ".join(category["items"])
            lines.append(f"**{label}:** {items}")
    return "\n".join(lines)


def generate(output_path: str = "output/linkedin_texts.md"):
    data = load_data()

    linkedin = data["linkedin"]
    personal = data["personal"]

    headline = linkedin["headline"]
    about = linkedin["about"]
    cta = linkedin["cta"]

    experience_section = _format_experience(data)
    skills_section = _format_skills(data)

    contact = f"{personal['email']} | t.me/{personal['telegram']}"

    content = f"""# LinkedIn Profile Texts

Ready-to-copy texts for LinkedIn profile.

## Headline (220 chars max)

{headline}

## About

{about}

{contact}

## Experience Descriptions

{experience_section}

## Recommended Skills

{skills_section}

## Call to Action

{cta}
"""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"LinkedIn texts generated: {path}")


if __name__ == "__main__":
    generate()
