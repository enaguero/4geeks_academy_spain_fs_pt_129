#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB_DIR="$ROOT_DIR/sqlite"
DB_FILE="${1:-$DB_DIR/day25.db}"

if ! command -v sqlite3 >/dev/null 2>&1; then
    echo "Error: sqlite3 no esta instalado. Instala sqlite3 y vuelve a intentarlo."
    exit 1
fi

if [ ! -f "$DB_FILE" ]; then
    echo "No existe la base: $DB_FILE"
    echo "Ejecuta primero scripts/db_init.sh"
    exit 1
fi

sqlite3 "$DB_FILE"
