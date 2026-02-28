#!/usr/bin/env python3
"""Generate GitHub profile README from data.json.

Follows 2025 best practices: one-screen max, professional, no badge walls,
no animated widgets, direct links to portfolio and resumes.
"""

import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / "data.json"
with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)


def generate(output_path: str = "README.md"):
    p = data["personal"]
    gh = p["github"]

    # Core tech badges (limited to ~10)
    badges = [
        ("Python", "3670A0", "python", "ffdd54"),
        ("Rust", "000000", "rust", "white"),
        ("Go", "00ADD8", "go", "white"),
        ("FastAPI", "005571", "fastapi", "white"),
        ("PostgreSQL", "316192", "postgresql", "white"),
        ("Redis", "DD0031", "redis", "white"),
        ("Docker", "0db7ed", "docker", "white"),
        ("Kubernetes", "326ce5", "kubernetes", "white"),
    ]
    badge_md = " ".join(
        f"![{n}](https://img.shields.io/badge/{n}-{bg}?style=flat-square&logo={l}&logoColor={fg})"
        for n, bg, l, fg in badges
    )

    readme = f"""## {p['name']}

**{data['titles']['portfolio']}** · {p['location']}

{data['summaries']['portfolio']}

{badge_md}

---

### What I've Built

- Microservices ecosystem: **200 rps**, **10K users**, **99% uptime** (Temporal.io, Elasticsearch, K8s)
- SDK generation pipeline: mitmproxy → OpenAPI → auto-generated SDK for **20+ exchange APIs**
- Wallet orchestrator: **2,000+ EVM wallets**, **5,000+ daily transactions**, zero manual intervention
- Market data pipeline: **260M+ candlesticks** collected for ML model training
- Rust-based POW solver: **20x performance improvement** over browser baseline

### Currently

- Completing **Stanford ML Specialization** and **NYIF ML in Trading** courses
- Building trading models on 260M+ datapoint dataset (PyTorch, LSTM/CNN)
- Open to **senior backend / infrastructure / ML engineering** roles

---

[![Portfolio](https://img.shields.io/badge/Portfolio-7c3aed?style=for-the-badge)](https://arkptz.github.io/{gh})
[![Resume: Backend](https://img.shields.io/badge/Resume_Backend-06b6d4?style=for-the-badge)](https://github.com/{gh}/{gh}/blob/main/output/Arkadiy_Pechnikov_Resume_Backend.pdf)
[![Resume: ML](https://img.shields.io/badge/Resume_ML-10b981?style=for-the-badge)](https://github.com/{gh}/{gh}/blob/main/output/Arkadiy_Pechnikov_Resume_ML.pdf)
[![Resume: Tech Lead](https://img.shields.io/badge/Resume_TechLead-f59e0b?style=for-the-badge)](https://github.com/{gh}/{gh}/blob/main/output/Arkadiy_Pechnikov_Resume_TechLead.pdf)

<a href="https://t.me/{p['telegram']}"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white" /></a>
<a href="https://linkedin.com/in/{p['linkedin']}"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" /></a>
<a href="mailto:{p['email']}"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>

<sub>{p['hiring_notice']}</sub>

<p align="center">
  <img src="game.gif" alt="GitHub Space Shooter" />
  <br/>
  <sub>🎮 My GitHub contributions as a Space Shooter game!</sub>
</p>

<p align="left">
  <img src="https://komarev.com/ghpvc/?username=arkptz&label=Profile%20views&color=0e75b6&style=flat" alt="arkptz" />
</p>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"README generated: {output_path}")


if __name__ == "__main__":
    generate()
