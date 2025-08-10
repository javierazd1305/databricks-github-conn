#!/usr/bin/env bash
set -euo pipefail

: "${DBX_USER:?Debe estar seteado (tu usuario de Databricks)}"

ENVIRONMENT="${1:-dev}"
TARGET="/Users/$DBX_USER/proj/$ENVIRONMENT"

echo "Creando carpeta destino en Workspace: $TARGET"
databricks workspace mkdirs "$TARGET"

echo "Importando notebooks/ a $TARGET/notebooks"
databricks workspace import-dir notebooks "$TARGET/notebooks" --overwrite

echo "Listando contenido"
databricks workspace list "$TARGET"
