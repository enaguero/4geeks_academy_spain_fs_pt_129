#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB_DIR="$ROOT_DIR/sqlite"
DB_FILE="${1:-$DB_DIR/day25.db}"

if ! command -v sqlite3 >/dev/null 2>&1; then
    echo "Error: sqlite3 no esta instalado. Instala sqlite3 y vuelve a intentarlo."
    exit 1
fi

case "$DB_FILE" in
    *.db) ;;
    *)
        echo "Error: la ruta de base de datos debe terminar en .db"
        exit 1
        ;;
esac

if [ -f "$DB_FILE" ]; then
    rm -f "$DB_FILE"
fi

"$ROOT_DIR/scripts/db_init.sh" "$DB_FILE"
