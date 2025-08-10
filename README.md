# Databricks CI/CD Minimal (Free Edition-friendly)

Este repo muestra un flujo **mínimo** de CI/CD con **GitHub Actions** y **Databricks CLI** que funciona en la **Free Edition** porque no lanza cómputo (no Jobs), solo valida acceso y **importa notebooks** al Workspace.

## Estructura

```
.
├─ notebooks/
│  ├─ 00_smoke_note.py
│  └─ etl/01_dummy_etl.py
├─ src/
│  └─ mypkg/__init__.py
├─ scripts/
│  └─ import_to_workspace.sh
├─ .github/workflows/
│  └─ databricks-smoke.yml
├─ requirements.txt
├─ .gitignore
└─ README.md
```

## Requisitos

1. Crear **Secrets** en GitHub (repo → Settings → Secrets and variables → Actions):
   - `DATABRICKS_HOST` → URL del workspace (p.ej. `https://<tu-workspace>.cloud.databricks.com`)
   - `DATABRICKS_TOKEN` → Personal Access Token del workspace
   - `DBX_USER` → Tu usuario en Databricks (normalmente tu email)

2. Tener un workspace con **Unity Catalog** habilitado (en Free Edition el catálogo visible suele ser `workspace`).

## Cómo usar

- **Ramas**: usa `dev` y `main`.
- Al hacer push a `dev` o `main`, el workflow:
  - Instala el CLI, autentica y hace checks (`current-user`, `catalogs list`, `workspace list /`).
  - Importa `notebooks/` a:
    - `/Users/$DBX_USER/proj/dev/notebooks` si la rama es `dev`
    - `/Users/$DBX_USER/proj/prod/notebooks` si la rama es `main`

También puedes lanzar el workflow manualmente con **Run workflow** (evento `workflow_dispatch`).

## Import manual desde tu máquina (opcional)

```bash
export DATABRICKS_HOST="https://<tu-workspace>.cloud.databricks.com"
export DATABRICKS_TOKEN="<tu-token>"
databricks auth env --host "$DATABRICKS_HOST" --token "$DATABRICKS_TOKEN"

export DBX_USER="<tu-usuario>"
bash scripts/import_to_workspace.sh dev
```

## Siguientes pasos

- Añade otro workflow para validar estilo/lint o tests unitarios de `src/`.
- Si más adelante pasas a un workspace con Jobs, puedes incluir un step que ejecute un notebook como smoke test.
