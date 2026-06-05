[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 2: Migrations (`Flask-Migrate` + Alembic)

## 🎯 Goal

Understand what migrations are and run their full workflow: creating, applying, and reverting schema changes.

---

## 1) What is a migration?

A migration is a versioned file that describes how the database schema changes over time.

Example schema changes:

- adding an `avatar_url` column,
- creating a `favorites` table,
- adding a `UNIQUE` index on `email`.

Without migrations, each student can end up with a different database.

---

## 2) What tools do we use in Flask?

- `Flask-Migrate`: integrates `flask db ...` commands into your app.
- `Alembic`: the engine that generates and runs migration scripts.
- `Flask-SQLAlchemy`: defines models and metadata.

---

## 3) Minimal setup

Install dependencies:

```bash
pip install -r day_26/requirements.txt
```

App file ready for migrations:

- `day_26/example_app.py`

---

## 4) Key commands (create and run migrations)

From the repo root:

```bash
flask --app day_26/example_app.py db init
flask --app day_26/example_app.py db migrate -m "initial schema"
flask --app day_26/example_app.py db upgrade
```

Meaning:

- `db init`: creates the `migrations/` folder (only once per project).
- `db migrate`: detects differences between the models and the current schema.
- `db upgrade`: applies the pending migration to the database.

---

## 5) Revert and audit

```bash
flask --app day_26/example_app.py db downgrade
flask --app day_26/example_app.py db current
flask --app day_26/example_app.py db history
```

- `downgrade`: reverts one version (or to a specific revision id).
- `current`: shows the current revision of the database.
- `history`: lists the migration history.

---

## 6) Recommended workflow in class

1. You change the models.
2. You run `db migrate -m "describe change"`.
3. You review the generated script in `migrations/versions/`.
4. You run `db upgrade`.
5. You run tests or endpoints to validate.
6. You commit code + migration in the same PR.

---

## 7) Common mistakes

- Changing models and forgetting `db upgrade`.
- Generating a migration with models not imported in the app.
- Editing the database manually and breaking Alembic's history.
- Pushing code without the migration files.

---

## ✅ Step Checklist

- [ ] I can explain what problem migrations solve.
- [ ] I can create a migration with a clear message.
- [ ] I can apply a migration and verify the result.
- [ ] I know how to revert a migration when something goes wrong.
