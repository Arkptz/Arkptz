#!/usr/bin/env python3
"""Generate portfolio website from data.json for GitHub Pages."""

import json
import shutil
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent
DATA_PATH = ROOT_DIR / "data.json"
OUTPUT_DIR = ROOT_DIR / "output" / "portfolio"
TEMPLATE_DIR = SCRIPT_DIR / "template"


def load_data():
    """Load data from JSON."""
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def generate_html(data: dict) -> str:
    """Generate complete HTML portfolio."""

    p = data["personal"]
    meta = data["meta"]
    skills = data["skills"]
    experience = data["experience"]
    projects = data.get("projects", [])
    education = data["education"]
    stats = data.get("stats", [])
    social = data.get("social", {})

    # Generate skills HTML
    skills_html = ""
    for key, skill_data in skills.items():
        items = skill_data["items"]
        skills_html += f"""
            <div class="skill-category">
                <h4>{skill_data['label']}</h4>
                <div class="skill-tags">
                    {"".join(f'<span class="skill-tag">{item}</span>' for item in items)}
                </div>
            </div>
        """

    # Generate experience HTML
    experience_html = ""
    for job in experience:
        company_line = job["company"]
        if job.get("period"):
            company_line += f" | {job['period']}"
        if job.get("location"):
            company_line += f" | {job['location']}"

        bullets = "".join(f'<li>{bullet}</li>' for bullet in job["bullets"])
        tech = ", ".join(job.get("tech", []))

        experience_html += f"""
            <div class="experience-item">
                <h4>{job['title']}</h4>
                <p class="company">{company_line}</p>
                <ul>{bullets}</ul>
                <p class="tech"><strong>Tech:</strong> {tech}</p>
            </div>
        """

    # Generate projects HTML
    projects_html = ""
    for proj in projects:
        if not proj.get("featured", True):
            continue

        metrics_html = "".join(
            f'<div class="metric"><span class="metric-value">{m["value"]}</span><span class="metric-label">{m["label"]}</span></div>'
            for m in proj.get("metrics", [])
        )

        tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in proj.get("tech", []))

        projects_html += f"""
            <div class="project-card">
                <h4>{proj['title']}</h4>
                <p>{proj['description']}</p>
                <div class="metrics">{metrics_html}</div>
                <div class="tech-tags">{tech_html}</div>
            </div>
        """

    # Generate stats HTML
    stats_html = "".join(
        f'''<div class="stat">
            <span class="stat-value">{s["value"]}{s.get("suffix", "")}</span>
            <span class="stat-label">{s["label"]}</span>
        </div>'''
        for s in stats
    )

    # Generate education HTML
    education_html = ""
    for edu in education:
        education_html += f"""
            <div class="education-item">
                <h4>{edu['title']}</h4>
                <p>{edu['institution']} — {edu['status']}</p>
            </div>
        """

    # Social links
    social_html = ""
    if social.get("github"):
        social_html += f'<a href="{social["github"]}" class="social-link" target="_blank" rel="noopener">GitHub</a>'
    if social.get("telegram"):
        social_html += f'<a href="{social["telegram"]}" class="social-link" target="_blank" rel="noopener">Telegram</a>'
    if social.get("linkedin"):
        social_html += f'<a href="{social["linkedin"]}" class="social-link" target="_blank" rel="noopener">LinkedIn</a>'
    if social.get("email"):
        social_html += f'<a href="{social["email"]}" class="social-link">Email</a>'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta['title']}</title>
    <meta name="description" content="{meta['description']}">
    <meta name="keywords" content="{meta['keywords']}">
    <meta name="theme-color" content="{meta.get('theme_color', '#7c3aed')}">
    <meta property="og:title" content="{meta['title']}">
    <meta property="og:description" content="{meta['description']}">
    <meta property="og:type" content="website">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #0a0a0f;
            --bg-secondary: #12121a;
            --bg-card: #1a1a25;
            --text-primary: #ffffff;
            --text-secondary: #a0a0b0;
            --accent-primary: #7c3aed;
            --accent-secondary: #06b6d4;
            --border: #2a2a3a;
            --gradient: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        /* Background animation */
        .bg-gradient {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                radial-gradient(ellipse at 20% 20%, rgba(124, 58, 237, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(6, 182, 212, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
        }}

        /* Navigation */
        nav {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 1rem 2rem;
            background: rgba(10, 10, 15, 0.8);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .nav-logo {{
            font-weight: 700;
            font-size: 1.25rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .nav-links {{
            display: flex;
            gap: 2rem;
        }}

        .nav-links a {{
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.9rem;
            transition: color 0.3s;
        }}

        .nav-links a:hover {{
            color: var(--text-primary);
        }}

        .nav-cta {{
            background: var(--gradient);
            color: white;
            padding: 0.5rem 1.25rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: opacity 0.3s;
        }}

        .nav-cta:hover {{
            opacity: 0.9;
        }}

        /* Hero */
        .hero {{
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 6rem 2rem 4rem;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 2rem;
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }}

        .hero-badge .dot {{
            width: 8px;
            height: 8px;
            background: #22c55e;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}

        .hero h1 {{
            font-size: clamp(2.5rem, 8vw, 5rem);
            font-weight: 800;
            line-height: 1.1;
            margin-bottom: 1rem;
        }}

        .hero h1 .gradient {{
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .hero-subtitle {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 1.25rem;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }}

        .hero-description {{
            max-width: 600px;
            color: var(--text-secondary);
            margin-bottom: 2rem;
        }}

        .hero-contact {{
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-bottom: 2rem;
            font-size: 0.9rem;
            color: var(--text-secondary);
        }}

        .hero-contact a {{
            color: var(--text-secondary);
            text-decoration: none;
            transition: color 0.3s;
        }}

        .hero-contact a:hover {{
            color: var(--accent-primary);
        }}

        .hero-buttons {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        }}

        .btn-primary {{
            background: var(--gradient);
            color: white;
            padding: 0.875rem 2rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: 500;
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 40px rgba(124, 58, 237, 0.3);
        }}

        .btn-secondary {{
            background: var(--bg-card);
            color: var(--text-primary);
            padding: 0.875rem 2rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: 500;
            border: 1px solid var(--border);
            transition: border-color 0.3s;
        }}

        .btn-secondary:hover {{
            border-color: var(--accent-primary);
        }}

        /* Resume Downloads */
        .resume-downloads {{
            margin-top: 2rem;
            text-align: center;
        }}

        .resume-label {{
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
        }}

        .resume-buttons {{
            display: flex;
            gap: 0.75rem;
            flex-wrap: wrap;
            justify-content: center;
        }}

        .resume-btn {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 0.6rem 1rem;
            border-radius: 0.5rem;
            text-decoration: none;
            color: var(--text-primary);
            font-size: 0.85rem;
            transition: all 0.3s;
        }}

        .resume-btn:hover {{
            border-color: var(--accent-primary);
            background: var(--bg-secondary);
            transform: translateY(-2px);
        }}

        .resume-icon {{
            font-size: 1rem;
        }}

        .resume-text {{
            font-weight: 500;
        }}

        /* Sections */
        section {{
            padding: 5rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}

        .section-header {{
            text-align: center;
            margin-bottom: 3rem;
        }}

        .section-tag {{
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 2rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: var(--accent-primary);
            margin-bottom: 1rem;
        }}

        .section-title {{
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}

        .section-title .gradient {{
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        /* Stats */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1.5rem;
            margin-bottom: 4rem;
        }}

        .stat {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.3s, border-color 0.3s;
        }}

        .stat:hover {{
            transform: translateY(-5px);
            border-color: var(--accent-primary);
        }}

        .stat-value {{
            display: block;
            font-size: 2rem;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .stat-label {{
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}

        /* Skills */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }}

        .skill-category {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1.5rem;
        }}

        .skill-category h4 {{
            font-size: 1rem;
            margin-bottom: 1rem;
            color: var(--text-secondary);
        }}

        .skill-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .skill-tag {{
            background: var(--bg-secondary);
            padding: 0.4rem 0.8rem;
            border-radius: 2rem;
            font-size: 0.85rem;
            border: 1px solid var(--border);
            transition: border-color 0.3s;
        }}

        .skill-tag:hover {{
            border-color: var(--accent-primary);
        }}

        /* Experience */
        .experience-item {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }}

        .experience-item h4 {{
            font-size: 1.1rem;
            margin-bottom: 0.25rem;
        }}

        .experience-item .company {{
            color: var(--accent-primary);
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }}

        .experience-item ul {{
            list-style: none;
            margin-bottom: 1rem;
        }}

        .experience-item li {{
            position: relative;
            padding-left: 1.25rem;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        .experience-item li::before {{
            content: "›";
            position: absolute;
            left: 0;
            color: var(--accent-primary);
        }}

        .experience-item .tech {{
            font-size: 0.85rem;
            color: var(--text-secondary);
        }}

        /* Projects */
        .projects-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 1.5rem;
        }}

        .project-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1.5rem;
            transition: transform 0.3s, border-color 0.3s;
        }}

        .project-card:hover {{
            transform: translateY(-5px);
            border-color: var(--accent-primary);
        }}

        .project-card h4 {{
            font-size: 1.1rem;
            margin-bottom: 0.75rem;
        }}

        .project-card p {{
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }}

        .metrics {{
            display: flex;
            gap: 1rem;
            margin-bottom: 1rem;
        }}

        .metric {{
            text-align: center;
        }}

        .metric-value {{
            display: block;
            font-weight: 700;
            color: var(--accent-secondary);
        }}

        .metric-label {{
            font-size: 0.75rem;
            color: var(--text-secondary);
        }}

        .tech-tags {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
        }}

        .tech-tag {{
            background: var(--bg-secondary);
            padding: 0.25rem 0.6rem;
            border-radius: 2rem;
            font-size: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
            color: var(--text-secondary);
        }}

        /* Education */
        .education-item {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1.25rem;
            margin-bottom: 1rem;
        }}

        .education-item h4 {{
            font-size: 1rem;
            margin-bottom: 0.25rem;
        }}

        .education-item p {{
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        /* Contact */
        .contact-section {{
            text-align: center;
        }}

        .social-links {{
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 2rem;
        }}

        .social-link {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            color: var(--text-primary);
            text-decoration: none;
            transition: border-color 0.3s, transform 0.3s;
        }}

        .social-link:hover {{
            border-color: var(--accent-primary);
            transform: translateY(-2px);
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 3rem 2rem;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            font-size: 0.9rem;
        }}

        footer a {{
            color: var(--accent-primary);
            text-decoration: none;
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            .nav-links {{ display: none; }}
            .hero h1 {{ font-size: 2.5rem; }}
            section {{ padding: 3rem 1rem; }}
            .stats-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
    </style>
</head>
<body>
    <div class="bg-gradient"></div>

    <nav>
        <div class="nav-logo">AP</div>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#experience">Experience</a>
            <a href="#projects">Projects</a>
        </div>
        <a href="#contact" class="nav-cta">Contact</a>
    </nav>

    <header class="hero">
        <div class="hero-badge">
            <span class="dot"></span>
            Available for opportunities
        </div>
        <h1>
            {p['name'].split()[0]}<br>
            <span class="gradient">{p['name'].split()[-1]}</span>
        </h1>
        <p class="hero-subtitle">&gt; {data['titles']['portfolio']}</p>
        <p class="hero-description">{p.get('tagline', '')}</p>
        <div class="hero-contact">
            <span>📍 {p['location']} ({p['open_to']})</span>
            <span>✉️ <a href="mailto:{p['email']}">{p['email']}</a></span>
            <span>💻 <a href="https://github.com/{p['github']}" target="_blank">github.com/{p['github']}</a></span>
        </div>
        <div class="hero-buttons">
            <a href="#contact" class="btn-primary">Get in Touch</a>
            <a href="https://github.com/{p['github']}" class="btn-secondary" target="_blank" rel="noopener">View GitHub</a>
        </div>

        <div class="resume-downloads">
            <p class="resume-label">📄 Download Resume:</p>
            <div class="resume-buttons">
                <a href="https://github.com/{p['github']}/Arkptz/raw/main/output/Arkadiy_Pechnikov_Resume_Backend.pdf" class="resume-btn" target="_blank">
                    <span class="resume-icon">⚡</span>
                    <span class="resume-text">Backend</span>
                </a>
                <a href="https://github.com/{p['github']}/Arkptz/raw/main/output/Arkadiy_Pechnikov_Resume_ML.pdf" class="resume-btn" target="_blank">
                    <span class="resume-icon">🤖</span>
                    <span class="resume-text">ML</span>
                </a>
                <a href="https://github.com/{p['github']}/Arkptz/raw/main/output/Arkadiy_Pechnikov_Resume_Quant.pdf" class="resume-btn" target="_blank">
                    <span class="resume-icon">📈</span>
                    <span class="resume-text">Quant</span>
                </a>
            </div>
        </div>
    </header>

    <section id="about">
        <div class="section-header">
            <span class="section-tag">&lt;about /&gt;</span>
            <h2 class="section-title">Building <span class="gradient">High-Performance</span> Systems</h2>
            <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto;">{data['summaries']['portfolio']}</p>
        </div>

        <div class="stats-grid">
            {stats_html}
        </div>
    </section>

    <section id="skills">
        <div class="section-header">
            <span class="section-tag">&lt;skills /&gt;</span>
            <h2 class="section-title">Technical <span class="gradient">Expertise</span></h2>
        </div>

        <div class="skills-grid">
            {skills_html}
        </div>
    </section>

    <section id="experience">
        <div class="section-header">
            <span class="section-tag">&lt;experience /&gt;</span>
            <h2 class="section-title">Work <span class="gradient">Experience</span></h2>
        </div>

        {experience_html}
    </section>

    <section id="projects">
        <div class="section-header">
            <span class="section-tag">&lt;projects /&gt;</span>
            <h2 class="section-title">Featured <span class="gradient">Projects</span></h2>
        </div>

        <div class="projects-grid">
            {projects_html}
        </div>
    </section>

    <section id="education">
        <div class="section-header">
            <span class="section-tag">&lt;education /&gt;</span>
            <h2 class="section-title">Continuous <span class="gradient">Learning</span></h2>
        </div>

        {education_html}
    </section>

    <section id="contact" class="contact-section">
        <div class="section-header">
            <span class="section-tag">&lt;contact /&gt;</span>
            <h2 class="section-title">Let's <span class="gradient">Connect</span></h2>
            <p style="color: var(--text-secondary); max-width: 500px; margin: 0 auto;">
                Open to remote opportunities and interesting projects.
                Let's discuss how I can help build your next high-performance system.
            </p>
        </div>

        <div class="social-links">
            {social_html}
        </div>
    </section>

    <footer>
        <p>Made with ❤️ using Python & data.json</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem;">
            Auto-generated from <a href="https://github.com/Arkptz/Arkptz">Arkptz/Arkptz</a>
        </p>
    </footer>
</body>
</html>'''

    return html


def generate(output_dir: str = None):
    """Generate portfolio website."""
    if output_dir is None:
        output_dir = OUTPUT_DIR

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load data
    data = load_data()

    # Generate HTML
    html = generate_html(data)

    # Write index.html
    index_path = output_path / "index.html"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Portfolio generated: {index_path}")
    return str(index_path)


if __name__ == "__main__":
    generate()
