# Resume Generator

PDF resume generator + GitHub profile README + portfolio site from a single `data.json`.

## Structure

```
├── data.json                        # All data (personal, experience, skills)
├── resume_generator/
│   ├── generate_all.py              # Generate everything
│   ├── generate_backend.py          # Backend-focused resume
│   ├── generate_ml.py               # ML-focused resume
│   ├── generate_techlead.py         # Tech Lead resume
│   ├── generate_readme.py           # GitHub profile README
│   ├── generate_portfolio.py        # Portfolio website data.js
│   └── shared.py                    # Shared PDF styles and utilities
├── output/                          # Generated files
│   ├── *.pdf                        # Resume PDFs
│   └── portfolio/                   # Portfolio website
│       ├── index.html               # Terminal-themed portfolio
│       └── data.js                  # Auto-generated from data.json
└── pyproject.toml                   # uv project config
```

## Usage

```bash
uv sync
uv run generate-resume
```

Or generate individually:

```bash
uv run generate-backend
uv run generate-ml
uv run generate-techlead
uv run generate-portfolio
```

## What gets generated

- `Arkadiy_Pechnikov_Resume_Backend.pdf`
- `Arkadiy_Pechnikov_Resume_ML.pdf`
- `Arkadiy_Pechnikov_Resume_TechLead.pdf`
- `README.md` (GitHub profile)
- `output/portfolio/data.js` (portfolio website data)

## Single source of truth

Edit `data.json` once, regenerate everything:

```json
{
  "personal": { "name", "email", "hiring_notice", ... },
  "titles": { "backend", "ml", "techlead", "portfolio" },
  "summaries": { "backend", "ml", "techlead", "portfolio" },
  "skills": { ... },
  "experience": [ ... ],
  "education": [ ... ]
}
```

## GitHub Actions

Three workflows automate the pipeline:

- **generate-resumes.yml** — on push to `data.json` or `resume-generator/`, regenerates all PDFs, README, and portfolio data, then commits back to repo
- **pages.yml** — on push to `output/portfolio/`, deploys portfolio to GitHub Pages
- **update-game.yml** — daily cron, regenerates `game.gif` from GitHub contribution graph
