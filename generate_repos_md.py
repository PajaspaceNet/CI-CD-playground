import requests

# GitHub username
username = "PajaspaceNet"  # ← nahraď svým jménem

# Získání veřejných repozitářů (žádná autentizace)
url = f"https://api.github.com/users/{username}/repos?per_page=100"
response = requests.get(url)

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
