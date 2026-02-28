#!/usr/bin/env python3
"""Generate backend-focused PDF resume."""

from shared import (
    load_data, build_styles, make_doc,
    add_header, add_summary, add_skills, add_experience,
    add_education, add_languages,
)

SKILL_KEYS = ["languages", "backend", "databases", "infrastructure", "monitoring", "blockchain"]


def generate(output_path: str = "Arkadiy_Pechnikov_Resume_Backend.pdf"):
    data = load_data()
    doc = make_doc(output_path)
    styles = build_styles()
    story = []

    add_header(story, data, "backend", styles)
    add_summary(story, data, "backend", styles)
    add_skills(story, data, SKILL_KEYS, styles)
    add_experience(story, data, "bullets_backend", styles)
    add_education(story, data, styles)
    add_languages(story, data, styles)

    doc.build(story)
    print(f"Backend resume: {output_path}")


if __name__ == "__main__":
    generate()
