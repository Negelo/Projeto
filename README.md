# Projeto Django - Trabalho de Administração de Sistemas

Este repositório contém uma aplicação Django desenvolvida para o trabalho prático.

## Repositório
- URL: https://github.com/Negelo/Projeto
- Branch principal: `main`

## Funcionalidades da app
- Aplicação Django com 3 páginas principais: `/`, `/publicacoes/`, `/utilizadores/`
- Dados dinâmicos vindos da base de dados via ORM
- Modelos: `Utilizador`, `Publicacao`, `Comentario`

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
- Não versionar `.env` real.
- Usar os exemplos:
  - `.env.dev.example` para desenvolvimento
  - `.env.prod.example` para produção
  - `.env.example` como base genérica

## Desenvolvimento vs Produção
### Desenvolvimento
- `DJANGO_DEBUG=True`
- Pode usar SQLite local para rapidez

### Produção
- `DJANGO_DEBUG=False`
- Usar MySQL
- Executar com `gunicorn`

## Base de dados MySQL
Variáveis necessárias:
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

Run:
```bash
docker run --rm -p 8000:8000 --env-file .env projeto-django
```

## Docker Compose
Subir serviços (Django + MySQL):
```bash
docker compose up --build
```

Parar:
```bash
docker compose down
```

## Requerimentos cumpridos
- Controlo de versões com Git + GitHub
- Ambiente virtual Python e dependências
- Aplicação Django criada e desenvolvida
- Variáveis de ambiente configuradas
- Dockerfile configurado
- Base de dados MySQL configurada
- Docker Compose com `web` + `db`

## Nota
Neste ambiente automático não foi possível executar Python localmente (runtime indisponível), por isso as estruturas Django e migração inicial foram preparadas de forma manual e versionadas.
