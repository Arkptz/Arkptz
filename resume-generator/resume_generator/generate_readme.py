#!/usr/bin/env python3

from .shared import load_data


def generate(output_path: str = "README.md"):
    data = load_data()
    personal = data.get("personal", {})
    social = data.get("social", {})
    readme = data.get("readme", {})

    name = personal.get("name", "")

    portfolio_url = social.get("github", "")
    if portfolio_url.startswith("https://github.com/"):
        github_user = portfolio_url.rstrip("/").split("/")[-1]
        portfolio_url = f"https://{github_user.lower()}.github.io/{github_user}"

    linkedin_url = social.get("linkedin", "")
    email_url = social.get("email", "")
    telegram_url = social.get("telegram", "")

    subtitle = readme.get("subtitle", "")
    currently = readme.get("currently", "")
    highlights = readme.get("highlights", [])
    stack = readme.get("stack", "")
    cta = readme.get("cta", "")

    highlights_md = "\n".join(f"- {h}" for h in highlights)

    content = f"""![](game.gif)

### {name}

{subtitle}

**Currently:** {currently}

**Recent work:**
{highlights_md}

**Stack:** {stack}

[Portfolio]({portfolio_url}) · [LinkedIn]({linkedin_url}) · [Email]({email_url}) · [Telegram]({telegram_url})
"""

    if cta:
        content = content.rstrip("\n") + f"\n\n> {cta}\n"

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"README generated: {output_path}")


if __name__ == "__main__":
    generate()
