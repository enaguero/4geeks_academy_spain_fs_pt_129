# Step 3: CRUD + JOINS (de simple a complejo)

## 🎯 Objetivo

Practicar consultas reales con SQLAlchemy ORM:

- `INSERT`
- `UPDATE`
- `SELECT`
- `DELETE`
- `JOIN` simple y múltiple
- `GROUP BY` + `HAVING`

---

## 1) Base de ejemplo

Modelos y app usados en este step:

- `day_26/example_app.py`
- `day_26/example_models.py`
- `day_26/example_queries.py`

---

## 2) INSERT de filas específicas

### ORM

```python
new_user = User(email="luis@example.com", username="luis_data")
new_user.profile = UserProfile(bio="Me interesan migraciones y joins")
db.session.add(new_user)
db.session.commit()
```

### SQL equivalente

```sql
INSERT INTO users (email, username, created_at)
VALUES ('luis@example.com', 'luis_data', CURRENT_TIMESTAMP);

INSERT INTO user_profiles (user_id, bio)
VALUES (LAST_INSERT_ROWID(), 'Me interesan migraciones y joins');
```

---

## 3) UPDATE de fila específica

### ORM

```python
user = db.session.get(User, 2)
if user is not None:
    user.email = "luis.orm@example.com"
    db.session.commit()
```

### SQL equivalente

```sql
UPDATE users
SET email = 'luis.orm@example.com'
WHERE id = 2;
```

---

## 4) SELECT simple y filtrado

### ORM

```python
stmt = select(User).where(User.username == "luis_data")
user = db.session.execute(stmt).scalar_one_or_none()
```

### SQL equivalente

```sql
SELECT id, email, username
FROM users
WHERE username = 'luis_data';
```

---

## 5) DELETE de fila específica

### ORM

```python
character = db.session.execute(
    select(Character).where(Character.name == "Leia Organa")
).scalar_one_or_none()

if character is not None:
    db.session.delete(character)
    db.session.commit()
```

### SQL equivalente

```sql
DELETE FROM characters
WHERE name = 'Leia Organa';
```

---

## 6) JOIN simple (`Character` + `Planet`)

### ORM

```python
stmt = (
    select(Character.name, Planet.name.label("planet_name"))
    .join(Planet, Character.planet_id == Planet.id)
    .order_by(Character.name.asc())
)
rows = db.session.execute(stmt).all()
```

### SQL equivalente

```sql
SELECT c.name, p.name AS planet_name
FROM characters c
JOIN planets p ON c.planet_id = p.id
ORDER BY c.name ASC;
```

---

## 7) JOIN múltiple con `LEFT JOIN`

Caso: listar usuarios con perfil y personajes favoritos (si existen).

### ORM

```python
stmt = (
    select(User.username, UserProfile.bio, Character.name.label("favorite_character"))
    .join(UserProfile, UserProfile.user_id == User.id)
    .outerjoin(Favorite, Favorite.user_id == User.id)
    .outerjoin(Character, Character.id == Favorite.character_id)
    .order_by(User.username.asc(), Character.name.asc())
)
rows = db.session.execute(stmt).all()
```

### SQL equivalente

```sql
SELECT u.username, up.bio, c.name AS favorite_character
FROM users u
JOIN user_profiles up ON up.user_id = u.id
LEFT JOIN favorites f ON f.user_id = u.id
LEFT JOIN characters c ON c.id = f.character_id
ORDER BY u.username ASC, c.name ASC;
```

---

## 8) JOIN complejo + agregación (`GROUP BY` + `HAVING`)

Caso: personajes con al menos `N` usuarios que los marcaron como favorito.

### ORM

```python
stmt = (
    select(Character.name, func.count(Favorite.user_id).label("total_users"))
    .join(Favorite, Favorite.character_id == Character.id)
    .group_by(Character.id, Character.name)
    .having(func.count(Favorite.user_id) >= 1)
    .order_by(func.count(Favorite.user_id).desc(), Character.name.asc())
)
rows = db.session.execute(stmt).all()
```

### SQL equivalente

```sql
SELECT c.name, COUNT(f.user_id) AS total_users
FROM characters c
JOIN favorites f ON f.character_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(f.user_id) >= 1
ORDER BY total_users DESC, c.name ASC;
```

---

## 9) JOIN `N-N` (`Character` <-> `Film`)

### ORM

```python
stmt = (
    select(Film.title, Character.name)
    .join(Film.characters)
    .where(Film.title == "A New Hope")
    .order_by(Character.name.asc())
)
rows = db.session.execute(stmt).all()
```

### SQL equivalente

```sql
SELECT f.title, c.name
FROM films f
JOIN character_films cf ON cf.film_id = f.id
JOIN characters c ON c.id = cf.character_id
WHERE f.title = 'A New Hope'
ORDER BY c.name ASC;
```

---

## 10) Cómo ejecutar la demo completa

```bash
flask --app day_26/example_app.py db upgrade
python -m day_26.example_queries
```

El script ejecuta inserciones, actualización, selección, borrado y varios joins.

---

## ✅ Checklist de este step

- [ ] Inserté filas específicas con ORM.
- [ ] Actualicé una fila usando condición por `id`.
- [ ] Seleccioné datos con filtros simples.
- [ ] Eliminé una fila concreta de forma segura.
- [ ] Construí al menos 2 consultas con joins.
- [ ] Hice una consulta con agregación y `HAVING`.
