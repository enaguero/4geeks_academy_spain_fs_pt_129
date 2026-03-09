# Step 0: ORM y `Flask-SQLAlchemy`

## 🎯 Objetivo

Entender qué es un ORM, qué hace SQLAlchemy y por qué en Flask usamos `Flask-SQLAlchemy`.

---

## 1) ¿Qué es un ORM?

Un **ORM (Object Relational Mapper)** permite trabajar tablas SQL como clases Python.

En vez de escribir siempre:

```sql
SELECT * FROM users WHERE email = 'ana@example.com';
```

puedes expresar la consulta como objetos:

```python
User.query.filter_by(email="ana@example.com").first()
```

El ORM traduce esa intención a SQL real.

---

## 2) “Flask Alchemy” vs paquete real

En clase suele decirse "Flask Alchemy", pero técnicamente:

- **SQLAlchemy**: el ORM real y motor principal.
- **Flask-SQLAlchemy**: extensión que integra SQLAlchemy con Flask (`db`, config, sesión).
- **Flask-Migrate**: extensión para migraciones usando Alembic.

Resumen: el ORM es SQLAlchemy; en Flask lo usamos normalmente a través de `Flask-SQLAlchemy`.

---

## 3) ¿Por qué usar ORM en bootcamp?

- Menos fricción al pasar de Python a base de datos.
- Modelado más legible con clases y relaciones.
- Mejor integración con APIs Flask.
- Mantiene SQL disponible cuando necesitas consultas avanzadas.

---

## 4) Ejemplo mínimo de modelo

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

Mapa mental:

- `class User` -> tabla `users`
- `id`, `email` -> columnas
- instancia `User(...)` -> fila

```
user = User("student@4geeks.com")
```

---

## 5) Qué debes dominar antes de pasar al Step 1

- [ ] Diferencia entre SQL crudo y ORM.
- [ ] Qué hace SQLAlchemy y qué hace Flask-SQLAlchemy.
- [ ] Cómo se define un modelo con `db.Model`.
