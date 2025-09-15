import csv
from datetime import datetime

# Název souborů
csv_file = "repos.csv"
md_file = "repos.md"

# Načti CSV
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    columns = reader.fieldnames

# Začni Markdown soubor s hlavičkou a datem
md_lines = [
    f"Generated with GitHub Automate – {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "# Seznam repozitářů",
    ""
]

# Hlavička tabulky
md_lines.append("| " + " | ".join(columns) + " |")
md_lines.append("| " + " | ".join(["---"] * len(columns)) + " |")

# Přidej data s klikacími odkazy pro Name
for row in rows:
    row_data = []
    for col in columns:
        val = row[col] if row[col] else ""
        if col.lower() == "name":
            val = f"[{val}]({row['URL']})"
        row_data.append(val)
    md_lines.append("| " + " | ".join(row_data) + " |")

# Ulož Markdown
with open(md_file, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"{md_file} byl úspěšně vygenerován z {csv_file}!")
