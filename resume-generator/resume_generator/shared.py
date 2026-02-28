"""Shared styles and utilities for all resume generators."""

import json
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable

# Colors
PRIMARY = HexColor("#1a1a2e")
ACCENT = HexColor("#4a90d9")
TEXT = HexColor("#333333")
GREY = HexColor("#666666")

DATA_PATH = Path(__file__).parent.parent.parent / "data.json"


def load_data() -> dict:
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="Notice",
            fontSize=8,
            leading=10,
            fontName="Helvetica",
            textColor=ACCENT,
            alignment=TA_CENTER,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Name",
            fontSize=20,
            leading=24,
            textColor=PRIMARY,
            fontName="Helvetica-Bold",
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TitleHeader",
            fontSize=11,
            leading=13,
            textColor=ACCENT,
            fontName="Helvetica-Bold",
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Contact",
            fontSize=8.5,
            leading=11,
            textColor=GREY,
            fontName="Helvetica",
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeader",
            fontSize=10.5,
            leading=13,
            textColor=PRIMARY,
            fontName="Helvetica-Bold",
            spaceBefore=10,
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="JobTitle",
            fontSize=10,
            leading=12,
            textColor=PRIMARY,
            fontName="Helvetica-Bold",
            spaceBefore=7,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Company",
            fontSize=9,
            leading=11,
            textColor=ACCENT,
            fontName="Helvetica",
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletItem",
            fontSize=9,
            leading=12,
            textColor=TEXT,
            fontName="Helvetica",
            leftIndent=12,
            spaceAfter=1.5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Summary",
            fontSize=9,
            leading=12.5,
            textColor=TEXT,
            fontName="Helvetica",
            alignment=TA_JUSTIFY,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SkillLine",
            fontSize=8.5,
            leading=11,
            textColor=TEXT,
            fontName="Helvetica",
            spaceAfter=1.5,
        )
    )
    return styles


def make_doc(output_path: str) -> SimpleDocTemplate:
    return SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )


def add_header(story, data, title_key, styles):
    """Add name, title, contact info, and divider."""
    p = data["personal"]
    story.append(Paragraph(p["hiring_notice"], styles["Notice"]))
    story.append(Paragraph(p["name"], styles["Name"]))
    story.append(Paragraph(data["titles"][title_key], styles["TitleHeader"]))

    contact_parts = [
        p["location"],
        p["email"],
        f"github.com/{p['github']}",
        f"linkedin.com/in/{p['linkedin']}",
        f"t.me/{p['telegram']}",
    ]
    story.append(Paragraph(" | ".join(contact_parts), styles["Contact"]))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=0.75, color=ACCENT, spaceBefore=0, spaceAfter=6))


def add_summary(story, data, summary_key, styles):
    story.append(Paragraph("PROFESSIONAL SUMMARY", styles["SectionHeader"]))
    story.append(Paragraph(data["summaries"][summary_key], styles["Summary"]))


def add_skills(story, data, skill_keys, styles):
    story.append(Paragraph("TECHNICAL SKILLS", styles["SectionHeader"]))
    for key in skill_keys:
        if key in data["skills"]:
            s = data["skills"][key]
            story.append(
                Paragraph(
                    f"<b>{s['label']}:</b> {', '.join(s['items'])}",
                    styles["SkillLine"],
                )
            )


def add_experience(story, data, bullet_key, styles, max_bullets=None):
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionHeader"]))
    for job in data["experience"]:
        story.append(Paragraph(job["title"], styles["JobTitle"]))

        parts = [job["company"]]
        if job.get("product"):
            parts[0] += f' — {job["product"]}'
        if job.get("period"):
            parts.append(job["period"])
        if job.get("location"):
            parts.append(job["location"])
        story.append(Paragraph(" | ".join(parts), styles["Company"]))

        bullets = job.get(bullet_key, job.get("bullets", []))
        if max_bullets:
            bullets = bullets[:max_bullets]
        for b in bullets:
            story.append(Paragraph(f"\u2022 {b}", styles["BulletItem"]))

        if job.get("tech"):
            story.append(
                Paragraph(
                    f'<b>Tech:</b> {", ".join(job["tech"])}',
                    styles["BulletItem"],
                )
            )


def add_education(story, data, styles):
    story.append(Paragraph("PROFESSIONAL DEVELOPMENT", styles["SectionHeader"]))
    for edu in data["education"]:
        story.append(
            Paragraph(
                f'<b>{edu["title"]}</b> — {edu["institution"]} ({edu["status"]})',
                styles["BulletItem"],
            )
        )


def add_languages(story, data, styles):
    story.append(Paragraph("LANGUAGES", styles["SectionHeader"]))
    lang = data["languages"]
    story.append(
        Paragraph(
            f'Russian: {lang["russian"]} | English: {lang["english"]}',
            styles["BulletItem"],
        )
    )
