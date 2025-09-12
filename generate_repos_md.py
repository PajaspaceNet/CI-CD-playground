import csv

# Název CSV souboru
csv_file = "repos.csv"      # ← nahraj svůj CSV soubor
md_file = "repos.md"        # ← soubor, který se vytvoří

# Otevři CSV a načti řádky
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Zjisti názvy sloupců z CSV
columns = reader.fieldnames

# Začni Markdown soubor
md_lines = ["# Seznam repozitářů", ""]

# Vytvoření hlavičky tabulky
md_lines.append("| " + " | ".join(columns) + " |")
md_lines.append("| " + " | ".join(["---"] * len(columns)) + " |")

# Přidej řádky
for row in rows:
    md_lines.append("| " + " | ".join(row[col] if row[col] else "" for col in columns) + " |")

# Ulož do souboru
with open(md_file, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"{md_file} byl úspěšně vygenerován z {csv_file}!")
