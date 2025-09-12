# CI/CD Playground

Tento repozitář slouží jako **DevOps / CI/CD playground**, ukazuje ukázkové pipeline pro různé nástroje a workflow.

## Obsah

- **Jenkins**  
  - Ukázkový `Jenkinsfile` pipeline pro Terraform projekty  
  - Spouští `terraform init`, `terraform plan` a `terraform apply`  
  - `README.md` obsahuje stručný popis pipeline
  

- **GitHub Actions**  
  - `main.yml` ukazuje jednoduchou CI workflow pro Terraform  
  - Spouští stejné kroky jako Jenkins pipeline

- **GitLab CI/CD**  
  - `.gitlab-ci.yml` ukázková pipeline pro Terraform

## Použití

1. **Jenkins:**  
   - Nastav Jenkins server nebo použij Docker image Jenkins  
   - Vlož `Jenkinsfile` do pipeline a spusť build

2. **GitHub Actions:**  
   - Umísti `main.yml` do `.github/workflows/` a pushni do GitHub repa  
   - Workflow se spustí automaticky při pushi
   - Testovani softwaru  - cast testovaci striktury
<pre>
     CI-CD-playground/
├── .github/
│   └── workflows/
│       ├── tests.yml             # hlavní workflow pro testy
│       ├── black.yml             # workflow pro black (volitelné)
│       └── playground.yml        # experimentální workflow
├── src/
│   ├── __init__.py
│   ├── math_utils.py
│   └── playground/              # experimentální kód
│       └── exp_module.py
├── tests/
│   ├── test_math_utils.py
│   └── playground/
│       └── test_exp_module.py
├── requirements.txt
└── README.md
</pre>

## Navrh struktury vice projektu v jednom repu
* Každý projekt má svou složku (project1/, project2/, …).



<pre>
repo/
├── .github/
│   └── workflows/
│       ├── project1.yml
│       ├── project2.yml
│       └── playground.yml
├── project1/
│   ├── src/
│   └── tests/
├── project2/
│   ├── src/
│   └── tests/
├── project3/
│   └── ...
└── README.md
</pre>


*Každý workflow YAML může být nastaven tak, aby se spouštěl jen na změny v určité složce:
<pre>
on:
  push:
    paths:
      - 'project1/**'
  pull_request:
    paths:
      - 'project1/**'
</pre>

3. **GitLab CI/CD:**  
   - Umísti `.gitlab-ci.yml` do root repozitáře  
   - Pipeline se spustí automaticky při pushi do GitLab repa

## Cíl

- Demonstrovat **CI/CD pipelines** pro infrastrukturu jako kód (Terraform)  
- Poskytnout **ukázkový playground**, kde se dá experimentovat s různými nástroji  
- Slouží jako **vzdělávací materiál** pro DevOps, CI/CD a IAC
