#!/usr/bin/env python3
"""Generate ML-focused PDF resume."""

import json
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

# Load data
DATA_PATH = Path(__file__).parent.parent.parent / "data.json"
with open(DATA_PATH) as f:
    data = json.load(f)

# Colors
PRIMARY_COLOR = HexColor('#1a1a2e')
ACCENT_COLOR = HexColor('#4a90d9')
TEXT_COLOR = HexColor('#333333')
LIGHT_GREY = HexColor('#666666')


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='Notice',
        fontSize=9,
        leading=12,
        fontName='Helvetica-Bold',
        textColor=ACCENT_COLOR,
        alignment=TA_CENTER,
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name='Name',
        fontSize=22,
        leading=26,
        textColor=PRIMARY_COLOR,
        fontName='Helvetica-Bold',
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='JobTitleHeader',
        fontSize=12,
        leading=14,
        textColor=ACCENT_COLOR,
        fontName='Helvetica-Bold',
        spaceAfter=8
    ))

    styles.add(ParagraphStyle(
        name='Contact',
        fontSize=9,
        leading=12,
        textColor=LIGHT_GREY,
        fontName='Helvetica'
    ))

    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontSize=11,
        leading=14,
        textColor=PRIMARY_COLOR,
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='JobTitle',
        fontSize=10,
        leading=13,
        textColor=PRIMARY_COLOR,
        fontName='Helvetica-Bold',
        spaceBefore=8,
        spaceAfter=1
    ))

    styles.add(ParagraphStyle(
        name='Company',
        fontSize=9,
        leading=12,
        textColor=ACCENT_COLOR,
        fontName='Helvetica',
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='BulletText',
        fontSize=9,
        leading=12,
        textColor=TEXT_COLOR,
        fontName='Helvetica',
        leftIndent=12,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='Summary',
        fontSize=9,
        leading=13,
        textColor=TEXT_COLOR,
        fontName='Helvetica',
        alignment=TA_JUSTIFY,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='SkillCategory',
        fontSize=9,
        leading=12,
        textColor=TEXT_COLOR,
        fontName='Helvetica',
        spaceAfter=2
    ))

    return styles


def generate(output_path: str = "Arkadiy_Pechnikov_Resume_ML.pdf"):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=0.6*inch,
        leftMargin=0.6*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = build_styles()
    story = []

    p = data["personal"]

    # Hiring notice
    story.append(Paragraph(p["hiring_notice"], styles['Notice']))

    # Header
    story.append(Paragraph(p["name"], styles['Name']))
    story.append(Paragraph(data["titles"]["ml"], styles['JobTitleHeader']))

    contact = f"{p['location']} ({p['open_to']}) | {p['email']} | {p['phone']} | github.com/{p['github']} | t.me/{p['telegram']}"
    story.append(Paragraph(contact, styles['Contact']))

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT_COLOR, spaceBefore=0, spaceAfter=8))

    # Summary
    story.append(Paragraph("SUMMARY", styles['SectionHeader']))
    story.append(Paragraph(data["summaries"]["ml"], styles['Summary']))

    # Skills (ML focused)
    story.append(Paragraph("SKILLS", styles['SectionHeader']))
    skill_keys = ["languages", "ml_data", "backend", "monitoring", "infrastructure", "databases"]
    for key in skill_keys:
        if key in data["skills"]:
            s = data["skills"][key]
            story.append(Paragraph(f"<b>{s['label']}:</b> {', '.join(s['items'])}", styles['SkillCategory']))

    # Experience
    story.append(Paragraph("EXPERIENCE", styles['SectionHeader']))
    for job in data["experience"]:
        story.append(Paragraph(job["title"], styles['JobTitle']))
        company_line = job["company"]
        if job["period"]:
            company_line += f" | {job['period']}"
        if job["location"]:
            company_line += f" | {job['location']}"
        story.append(Paragraph(company_line, styles['Company']))

        for bullet in job["bullets"]:
            story.append(Paragraph(f"• {bullet}", styles['BulletText']))

        if job.get("tech"):
            story.append(Paragraph(f"<b>Tech:</b> {', '.join(job['tech'])}", styles['BulletText']))

    # Education
    story.append(Paragraph("EDUCATION &amp; CERTIFICATIONS", styles['SectionHeader']))
    for edu in data["education"]:
        story.append(Paragraph(f"<b>{edu['title']}</b> — {edu['institution']} ({edu['status']})", styles['BulletText']))

    # Languages
    story.append(Paragraph("LANGUAGES", styles['SectionHeader']))
    story.append(Paragraph(f"Russian — {data['languages']['russian']} | English — {data['languages']['english']}", styles['BulletText']))

    doc.build(story)
    print(f"ML resume created: {output_path}")


if __name__ == "__main__":
    generate()
