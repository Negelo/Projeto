# Projeto Django - Trabalho de Administração de Sistemas

Este repositório contém uma aplicação Django desenvolvida para o trabalho prático da unidade curricular.

## Objetivo
Implementar uma aplicação web com Django, base de dados MySQL, Docker e Docker Compose, com separação entre ambiente de desenvolvimento e produção.

## Estado atual
Estrutura inicial do projeto criada.
## Ambiente virtual e dependências

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Variáveis de ambiente
1. Criar um ficheiro `.env` na raiz do repositório (não é versionado).
2. Usar `.env.example` como referência.
3. Ajustar os valores de acordo com o ambiente (dev/prod).

## Configuração MySQL
Exemplo de configuração no `.env`:
- `DB_ENGINE=django.db.backends.mysql`
- `DB_NAME=projeto_db`
- `DB_USER=projeto_user`
- `DB_PASSWORD=projeto_password`
- `DB_HOST=db`
- `DB_PORT=3306`

## Dockerfile
Build da imagem:
```bash
docker build -t projeto-django .
```

Execução:
```bash
docker run --rm -p 8000:8000 --env-file .env projeto-django
```
