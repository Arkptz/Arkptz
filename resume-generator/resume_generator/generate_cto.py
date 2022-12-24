#!/usr/bin/env python3

from .shared import (
    add_education,
    add_experience,
    add_header,
    add_languages,
    add_leadership_section,
    add_skills,
    add_summary,
    build_styles,
    load_data,
    make_doc,
)

RESUME_NAME = "cto"
TITLE_VARIANT = "cto"


def generate(output_path: str = "Arkadiy_Pechnikov_Resume_CTO.pdf"):
    data = load_data()
    doc = make_doc(output_path)
    styles = build_styles()
    story = []

    add_header(story, data, RESUME_NAME, styles)
    add_summary(story, data, RESUME_NAME, styles)
    skill_keys = data.get("skills_by_resume", {}).get(RESUME_NAME, [])
    add_skills(story, data, skill_keys, styles)
    add_experience(story, data, RESUME_NAME, TITLE_VARIANT, styles)
    add_leadership_section(story, data, styles)
    add_education(story, data, styles)
    add_languages(story, data, styles)

    doc.build(story)
    print(f"Resume ({RESUME_NAME}): {output_path}")


if __name__ == "__main__":
    generate()
