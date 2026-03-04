DB_FILE ?= $(CURDIR)/sqlite/day25.db

.PHONY: help db-init db-reset db-blank db-shell db-demo

help:
	@echo "Comandos disponibles (day_25):"
	@echo "  make db-init   -> crea sqlite/day25.db con schema + seed"
	@echo "  make db-demo   -> ejecuta consultas de sqlite/practice.sql"
	@echo "  make db-shell  -> abre consola sqlite3 en la base"
	@echo "  make db-reset  -> borra y recrea la base con schema + seed"
	@echo "  make db-blank  -> deja la base vacia (sin tablas ni datos)"

db-init:
	./scripts/db_init.sh "$(DB_FILE)"

db-reset:
	./scripts/db_reset.sh "$(DB_FILE)"

db-blank:
	./scripts/db_blank.sh "$(DB_FILE)"

db-shell:
	./scripts/db_shell.sh "$(DB_FILE)"

db-demo:
	./scripts/db_query.sh "$(DB_FILE)" "$(CURDIR)/sqlite/practice.sql"
