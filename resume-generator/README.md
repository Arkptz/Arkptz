# Resume Generator

PDF resume generator + GitHub profile README from single `data.json`.

## Structure

```
├── data.json                    # All data (personal, experience, skills)
├── src/
│   ├── generate_all.py          # Generate everything
│   ├── generate_backend.py      # Backend-focused resume
│   ├── generate_ml.py           # ML-focused resume
│   ├── generate_quant.py        # Quant/trading resume
│   └── generate_readme.py       # GitHub profile README
├── output/                      # Generated files
└── pyproject.toml               # uv workspace config
```

## Usage

```bash
uv sync
uv run python src/generate_all.py
```

## What gets generated

- `Arkadiy_Pechnikov_Resume_Backend.pdf`
- `Arkadiy_Pechnikov_Resume_ML.pdf`
- `Arkadiy_Pechnikov_Resume_Quant.pdf`
- `README.md` (GitHub profile)

## Single source of truth

Edit `data.json` once, regenerate everything:

```json
{
  "personal": { "name", "email", "hiring_notice", ... },
  "titles": { "backend", "ml", "quant" },
  "summaries": { "backend", "ml", "quant" },
  "skills": { ... },
  "experience": [ ... ],
  "education": [ ... ]
}
```

## GitHub Actions

Auto-regenerates on push to `data.json` or `src/`. Commits updated PDFs and README back to repo.
