#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DB_DIR="$ROOT_DIR/sqlite"
DB_FILE="${1:-$DB_DIR/day25.db}"

case "$DB_FILE" in
    *.db) ;;
    *)
        echo "Error: la ruta de base de datos debe terminar en .db"
        exit 1
        ;;
esac

if [ -f "$DB_FILE" ]; then
    rm -f "$DB_FILE"
    echo "Base SQLite eliminada: $DB_FILE"
else
    echo "No existe la base: $DB_FILE"
fi
