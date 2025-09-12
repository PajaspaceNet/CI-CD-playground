import requests

# ← nahraď svým GitHub username
USERNAME = "PajaspaceNet"
OUTPUT_FILE = "repos.md"

# Stahování veřejných repozitářů
url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100"
repos = []
page = 1

while True:
    resp = requests.get(f"{url}&page={page}")
    data = resp.json()
    if not data:
        break
    for repo in data:
        name = repo["name"]
        html_url = repo["html_url"]
        description = repo.get("description", "")
        repos.append([name, html_url, description])
    page += 1

# Generování Markdown tabulky
md = "# Automaticky generovaný seznam mých repozitářů\n\n"
md += "| Název | Odkaz | Popis |\n|-------|-------|-------|\n"
for name, html_url, description in repos:
    md += f"| {name} | [Link]({html_url}) | {description} |\n"

# Uložení do repos.md
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(md)

print(f"✅ Uloženo {len(repos)} repozitářů do {OUTPUT_FILE}")
