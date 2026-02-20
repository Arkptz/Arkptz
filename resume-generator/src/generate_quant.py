#!/usr/bin/env python3
"""Generate Quant-focused PDF resume."""

import json
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER

# Load data
DATA_PATH = Path(__file__).parent.parent.parent / "data.json"
with open(DATA_PATH) as f:
    data = json.load(f)


def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='Notice',
        fontSize=9,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2E5090'),
        spaceAfter=12,
        spaceBefore=0
    ))

    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        fontSize=18,
        alignment=TA_CENTER,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='Subtitle',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_CENTER,
        textColor=colors.grey,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_CENTER,
        spaceAfter=12
    ))

    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#2E5090'),
        spaceBefore=12,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=styles['Normal'],
        fontSize=10,
        fontName='Helvetica-Bold',
        spaceBefore=6,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='JobDetails',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        spaceAfter=4
    ))

    styles.add(ParagraphStyle(
        name='BulletText',
        parent=styles['Normal'],
        fontSize=9,
        leftIndent=12,
        spaceAfter=2
    ))

    styles.add(ParagraphStyle(
        name='BodyText9',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=4
    ))

    return styles


def generate(output_path: str = "Arkadiy_Pechnikov_Resume_Quant.pdf"):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )

    styles = build_styles()
    story = []

    p = data["personal"]

    # Hiring notice
    story.append(Paragraph(p["hiring_notice"], styles['Notice']))

    # Header
    story.append(Paragraph(p["name"].upper(), styles['Name']))
    story.append(Paragraph(data["titles"]["quant"], styles['Subtitle']))

    contact = f"t.me/{p['telegram']} | {p['email']} | {p['phone']} | github.com/{p['github']}"
    story.append(Paragraph(contact, styles['Contact']))

    # Summary
    story.append(Paragraph("SUMMARY", styles['SectionHeader']))
    story.append(Paragraph(data["summaries"]["quant"], styles['BodyText9']))

    # Trading Experience
    story.append(Paragraph("TRADING EXPERIENCE", styles['SectionHeader']))
    for job in data["trading_experience"]:
        story.append(Paragraph(job["title"], styles['JobTitle']))
        period_line = job.get("company", "")
        if period_line and job["period"]:
            period_line += f" | {job['period']}"
        elif job["period"]:
            period_line = job["period"]
        if period_line:
            story.append(Paragraph(period_line, styles['JobDetails']))

        for bullet in job["bullets"]:
            story.append(Paragraph(f"• {bullet}", styles['BulletText']))

    # Quantitative Projects
    story.append(Paragraph("QUANTITATIVE PROJECTS", styles['SectionHeader']))
    for proj in data["quant_projects"]:
        story.append(Paragraph(proj["title"], styles['JobTitle']))
        for bullet in proj["bullets"]:
            story.append(Paragraph(f"• {bullet}", styles['BulletText']))

    # Technical Experience
    story.append(Paragraph("TECHNICAL EXPERIENCE", styles['SectionHeader']))
    for job in data["experience"][:2]:  # Only first 2 jobs
        story.append(Paragraph(f"{job['company']} | {job['title']}", styles['JobTitle']))
        story.append(Paragraph(job["period"], styles['JobDetails']))
        for bullet in job["bullets"][:3]:  # Only first 3 bullets
            story.append(Paragraph(f"• {bullet}", styles['BulletText']))

    # Skills
    story.append(Paragraph("SKILLS", styles['SectionHeader']))
    skill_keys = ["languages", "trading", "quant", "infrastructure", "databases"]
    for key in skill_keys:
        if key in data["skills"]:
            s = data["skills"][key]
            story.append(Paragraph(f"<b>{s['label']}:</b> {', '.join(s['items'])}", styles['BodyText9']))

    # Education
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", styles['SectionHeader']))
    for edu in data["education"]:
        story.append(Paragraph(f"<b>{edu['title']}</b> | {edu['status']}", styles['BodyText9']))

    # Languages
    story.append(Paragraph("LANGUAGES", styles['SectionHeader']))
    story.append(Paragraph(f"• Russian: {data['languages']['russian']}", styles['BulletText']))
    story.append(Paragraph(f"• English: {data['languages']['english']}", styles['BulletText']))

    doc.build(story)
    print(f"Quant resume created: {output_path}")


if __name__ == "__main__":
    generate()
