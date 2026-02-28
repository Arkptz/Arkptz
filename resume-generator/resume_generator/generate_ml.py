#!/usr/bin/env python3
"""Generate ML/Data-focused PDF resume."""

from .shared import (
    load_data,
    build_styles,
    make_doc,
    add_header,
    add_summary,
    add_skills,
    add_experience,
    add_education,
    add_languages,
)

SKILL_KEYS = ["languages", "ml_data", "backend", "databases", "monitoring", "infrastructure"]


def generate(output_path: str = "Arkadiy_Pechnikov_Resume_ML.pdf"):
    data = load_data()
    doc = make_doc(output_path)
    styles = build_styles()
    story = []

    add_header(story, data, "ml", styles)
    add_summary(story, data, "ml", styles)
    add_skills(story, data, SKILL_KEYS, styles)
    add_experience(story, data, "bullets_ml", styles)
    add_education(story, data, styles)
    add_languages(story, data, styles)

    doc.build(story)
    print(f"ML resume: {output_path}")


if __name__ == "__main__":
    generate()
