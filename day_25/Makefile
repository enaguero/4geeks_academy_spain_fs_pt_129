DB_FILE ?= $(CURDIR)/sqlite/day25.db

.PHONY: help db-schema db-seed db-setup db-drop db-reset db-shell db-init db-blank db-demo

help:
	@echo "Comandos disponibles (day_25):"
	@echo "  make db-schema -> crea sqlite/day25.db solo con schema (tablas)"
	@echo "  make db-seed   -> inserta datos de sqlite/seed.sql en la base"
	@echo "  make db-setup  -> recrea sqlite/day25.db con schema + seed"
	@echo "  make db-drop   -> elimina sqlite/day25.db"
	@echo "  make db-reset  -> ejecuta db-drop + db-setup"
	@echo "  make db-shell  -> abre consola sqlite3 en la base"
	@echo "  make db-demo   -> ejecuta consultas de sqlite/practice.sql"
	@echo "  make db-blank  -> deja la base vacia (sin tablas ni datos)"
	@echo "  make db-init   -> alias de db-schema (compatibilidad)"

db-schema:
	./scripts/db_init.sh "$(DB_FILE)"

db-seed:
	./scripts/db_seed.sh "$(DB_FILE)"

db-setup:
	./scripts/db_reset.sh "$(DB_FILE)"

db-drop:
	./scripts/db_drop.sh "$(DB_FILE)"

db-reset:
	@$(MAKE) db-drop DB_FILE="$(DB_FILE)"
	@$(MAKE) db-setup DB_FILE="$(DB_FILE)"

db-init:
	@$(MAKE) db-schema DB_FILE="$(DB_FILE)"

db-blank:
	./scripts/db_blank.sh "$(DB_FILE)"

db-shell:
	./scripts/db_shell.sh "$(DB_FILE)"

db-demo:
	./scripts/db_query.sh "$(DB_FILE)" "$(CURDIR)/sqlite/practice.sql"
