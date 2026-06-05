[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 0: ORM and `Flask-SQLAlchemy`

## 🎯 Goal

Understand what an ORM is, what SQLAlchemy does, and why in Flask we use `Flask-SQLAlchemy`.

---

## 1) What is an ORM?

An **ORM (Object Relational Mapper)** lets you work with SQL tables as if they were Python classes.

Instead of always writing:

```sql
SELECT * FROM users WHERE email = 'ana@example.com';
```

you can express the query as objects:

```python
User.query.filter_by(email="ana@example.com").first()
```

The ORM translates that intent into actual SQL.

---

## 2) "Flask Alchemy" vs the real package

In class people often say "Flask Alchemy", but technically:

- **SQLAlchemy**: the actual ORM and core engine.
- **Flask-SQLAlchemy**: extension that integrates SQLAlchemy with Flask (`db`, config, session).
- **Flask-Migrate**: extension for migrations using Alembic.

Summary: the ORM is SQLAlchemy; in Flask we normally use it through `Flask-SQLAlchemy`.

---

## 3) Why use an ORM in a bootcamp?

- Less friction when moving from Python to the database.
- More readable modeling with classes and relationships.
- Better integration with Flask APIs.
- Keeps SQL available when you need advanced queries.

---

## 4) Minimal model example

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

Mental map:

- `class User` -> `users` table
- `id`, `email` -> columns
- `User(...)` instance -> row

```
user = User("student@4geeks.com")
```

---

## 5) What you should master before moving to Step 1

- [ ] Difference between raw SQL and ORM.
- [ ] What SQLAlchemy does and what Flask-SQLAlchemy does.
- [ ] How to define a model with `db.Model`.
