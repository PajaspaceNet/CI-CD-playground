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

3. **GitLab CI/CD:**  
   - Umísti `.gitlab-ci.yml` do root repozitáře  
   - Pipeline se spustí automaticky při pushi do GitLab repa

## Cíl

- Demonstrovat **CI/CD pipelines** pro infrastrukturu jako kód (Terraform)  
- Poskytnout **ukázkový playground**, kde se dá experimentovat s různými nástroji  
- Slouží jako **vzdělávací materiál** pro DevOps, CI/CD a IAC
