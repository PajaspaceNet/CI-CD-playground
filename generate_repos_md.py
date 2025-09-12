import os
import requests

# Získání tokenu z prostředí
token = os.environ.get("GITHUB_TOKEN")
headers = {"Authorization": f"token {token}"} if token else {}

# GitHub username
username = "Pajaspacenet"  # <-- nahraď svým jménem

# URL pro získání repozitářů
url = f"https://api.github.com/users/{username}/repos?per_page=100"

response = requests.get(url, headers=headers)

if response.status_code != 200:
    raise Exception(f"Chyba při získávání repozitářů: {response.status_code} {response.text}")

repos = response.json()

# Vytvoření Markdown tabulky
md_lines = ["# Seznam mých GitHub repozitářů", "", "| Název | Popis | Link |", "| --- | --- | --- |"]

for repo in repos:
    name = repo["name"]
    desc = repo["description"] or ""
    link = repo["html_url"]
    md_lines.append(f"| {name} | {desc} | [Repo]({link}) |")

# Uložení do souboru
with open("repos.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("repos.md byl úspěšně vygenerován!")
