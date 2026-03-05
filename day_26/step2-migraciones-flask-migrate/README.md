# Step 2: Migraciones (`Flask-Migrate` + Alembic)

## 🎯 Objetivo

Entender qué son migraciones y ejecutar su flujo completo: crear, aplicar y revertir cambios de esquema.

---

## 1) ¿Qué es una migración?

Una migración es un archivo versionado que describe cómo cambia el esquema de la base de datos en el tiempo.

Ejemplo de cambio de esquema:

- agregar columna `avatar_url`,
- crear tabla `favorites`,
- agregar índice `UNIQUE` en `email`.

Sin migraciones, cada estudiante puede terminar con una base distinta.

---

## 2) ¿Qué herramientas usamos en Flask?

- `Flask-Migrate`: integra comandos `flask db ...` en tu app.
- `Alembic`: motor que genera y ejecuta scripts de migración.
- `Flask-SQLAlchemy`: define modelos y metadata.

---

## 3) Preparación mínima

Instalar dependencias:

```bash
pip install -r day_26/requirements.txt
```

Archivo de app listo para migraciones:

- `day_26/example_app.py`

---

## 4) Comandos clave (crear y correr migraciones)

Desde la raíz del repo:

```bash
flask --app day_26/example_app.py db init
flask --app day_26/example_app.py db migrate -m "initial schema"
flask --app day_26/example_app.py db upgrade
```

Significado:

- `db init`: crea carpeta `migrations/` (una sola vez por proyecto).
- `db migrate`: detecta diferencias entre modelos y esquema actual.
- `db upgrade`: aplica la migración pendiente a la base.

---

## 5) Revertir y auditar

```bash
flask --app day_26/example_app.py db downgrade
flask --app day_26/example_app.py db current
flask --app day_26/example_app.py db history
```

- `downgrade`: revierte una versión (o a un revision id específico).
- `current`: muestra la revisión actual de la base.
- `history`: lista historial de migraciones.

---

## 6) Flujo de trabajo recomendado en clase

1. Cambias modelos.
2. Ejecutas `db migrate -m "describe cambio"`.
3. Revisas el script generado en `migrations/versions/`.
4. Ejecutas `db upgrade`.
5. Corres pruebas o endpoints para validar.
6. Commit de código + migración en el mismo PR.

---

## 7) Errores comunes

- Cambiar modelos y olvidar `db upgrade`.
- Generar migración con modelos no importados en la app.
- Editar la base manualmente y romper el historial de Alembic.
- Subir código sin archivos de migración.

---

## ✅ Checklist de este step

- [ ] Sé explicar qué problema resuelven las migraciones.
- [ ] Puedo crear una migración con mensaje claro.
- [ ] Puedo aplicar una migración y verificar el resultado.
- [ ] Sé revertir una migración cuando algo sale mal.
