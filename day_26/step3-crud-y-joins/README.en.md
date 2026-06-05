[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 3: CRUD + JOINS (from simple to complex)

## 🎯 Goal

Practice real queries with the SQLAlchemy ORM:

- `INSERT`
- `UPDATE`
- `SELECT`
- `DELETE`
- Simple and multiple `JOIN`
- `GROUP BY` + `HAVING`

---

## 📖 What is CRUD?

**CRUD** is the acronym for the four fundamental operations you can perform on persistent data:

| Letter | Operation | Meaning                              |
| ------ | --------- | ------------------------------------ |
| **C**  | Create    | Create new records                   |
| **R**  | Read      | Read/query existing records          |
| **U**  | Update    | Modify existing records              |
| **D**  | Delete    | Remove records                       |

### Why is it important?

Practically **every application that stores data** needs these four operations. Whether it's a social network, an e-commerce, or a blog — they all create, read, update, and delete data.

### 🔗 The CRUD → SQL → HTTP → ORM connection

The interesting part is that CRUD maps directly to:

- **SQL**: The commands the database understands
- **HTTP**: The methods REST APIs use
- **ORM**: Python/SQLAlchemy methods

| CRUD       | SQL           | HTTP Method     | SQLAlchemy ORM                    | Typical endpoint              |
| ---------- | ------------- | --------------- | --------------------------------- | ----------------------------- |
| **Create** | `INSERT INTO` | `POST`          | `db.session.add(obj)`             | `POST /users`                 |
| **Read**   | `SELECT`      | `GET`           | `db.session.execute(select(...))` | `GET /users` or `GET /users/1`|
| **Update** | `UPDATE`      | `PUT` / `PATCH` | `obj.field = new_value`           | `PUT /users/1`                |
| **Delete** | `DELETE`      | `DELETE`        | `db.session.delete(obj)`          | `DELETE /users/1`             |

> 💡 **Key insight**: When you build a REST API with Flask, each endpoint typically runs one of these CRUD operations against the database.

---

## 1) Example baseline

Models and app used in this step:

- `day_26/example_app.py`
- `day_26/example_models.py`
- `day_26/example_queries.py`

---

## 2) CREATE — INSERT specific rows

### What does it do?

Creates one or more new records in the database.

### When to use it?

- Registering new users
- Creating posts, comments, products
- Any "create new X" form

### In a REST API

Typically invoked with `POST /resource` and a body containing the new record's data.

### ORM

```python
new_user = User(email="luis@example.com", username="luis_data")
new_user.profile = UserProfile(bio="I'm interested in migrations and joins")
db.session.add(new_user)
db.session.commit()
```

### Equivalent SQL

```sql
INSERT INTO users (email, username, created_at)
VALUES ('luis@example.com', 'luis_data', CURRENT_TIMESTAMP);

INSERT INTO user_profiles (user_id, bio)
VALUES (LAST_INSERT_ROWID(), 'I am interested in migrations and joins');
```

---

## 3) UPDATE — Modify a specific row

### What does it do?

Modifies the values of one or more fields of an existing record.

### When to use it?

- Editing a user profile
- Changing the status of an order
- Updating any existing data

### In a REST API

Typically invoked with `PUT /resource/{id}` or `PATCH /resource/{id}`.

### ORM

```python
user = db.session.get(User, 2)
if user is not None:
    user.email = "luis.orm@example.com"
    db.session.commit()
```

### Equivalent SQL

```sql
UPDATE users
SET email = 'luis.orm@example.com'
WHERE id = 2;
```

---

## 4) READ — Simple and filtered SELECT

### What does it do?

Queries and retrieves records from the database, optionally with filters.

### When to use it?

- Showing a list of users
- Looking up a product by ID
- Filtering posts by category
- Any screen that displays data

### In a REST API

Typically invoked with `GET /resource` (list) or `GET /resource/{id}` (get one).

### ORM

```python
stmt = select(User).where(User.username == "luis_data")
user = db.session.execute(stmt).scalar_one_or_none()
```

### Equivalent SQL

```sql
SELECT id, email, username
FROM users
WHERE username = 'luis_data';
```

---

## 5) DELETE — Remove a specific row

### What does it do?

Permanently removes a record from the database.

### When to use it?

- Deleting a user account
- Removing a post or comment
- Removing a product from the catalog

### In a REST API

Typically invoked with `DELETE /resource/{id}`.

### ⚠️ Caution

DELETE is permanent. In production, consider using "soft delete" (marking as deleted via a `deleted_at` field instead of physically removing the row).

### ORM

```python
character = db.session.execute(
    select(Character).where(Character.name == "Leia Organa")
).scalar_one_or_none()

if character is not None:
    db.session.delete(character)
    db.session.commit()
```

### Equivalent SQL

```sql
DELETE FROM characters
WHERE name = 'Leia Organa';
```

---

## 🌐 CRUD in Flask: full REST endpoints

Here are examples of how each CRUD operation looks implemented as a Flask endpoint:

### Initial setup

```python
from flask import Flask, request, jsonify
from sqlalchemy import select
from day_26.example_app import create_app, db
from day_26.example_models import User, UserProfile

app = create_app()
```

### POST /users — Create

```python
@app.route('/users', methods=['POST'])
def create_user():
    body = request.get_json()

    # Basic validation
    if not body or 'email' not in body or 'username' not in body:
        return jsonify({"error": "email and username are required"}), 400

    # Check if it already exists
    existing = db.session.execute(
        select(User).where(User.email == body['email'])
    ).scalar_one_or_none()

    if existing:
        return jsonify({"error": "The email is already registered"}), 400

    # Create user
    new_user = User(email=body['email'], username=body['username'])
    if 'bio' in body:
        new_user.profile = UserProfile(bio=body['bio'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "email": new_user.email,
        "username": new_user.username
    }), 201
```

### GET /users/{id} — Read

```python
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.get(User, user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "bio": user.profile.bio if user.profile else None
    }), 200
```

### PUT /users/{id} — Update

```python
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = db.session.get(User, user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    body = request.get_json()

    # Update fields if present in the body
    if 'email' in body:
        user.email = body['email']
    if 'username' in body:
        user.username = body['username']
    if 'bio' in body:
        if user.profile:
            user.profile.bio = body['bio']
        else:
            user.profile = UserProfile(bio=body['bio'])

    db.session.commit()

    return jsonify({
        "id": user.id,
        "email": user.email,
        "username": user.username
    }), 200
```

### DELETE /users/{id} — Delete

```python
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.session.get(User, user_id)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200
```

### HTTP status code summary

| Operation     | Success       | Common error                        |
| ------------- | ------------- | ----------------------------------- |
| POST (Create) | `201 Created` | `400 Bad Request` (invalid data)    |
| GET (Read)    | `200 OK`      | `404 Not Found`                     |
| PUT (Update)  | `200 OK`      | `404 Not Found`                     |
| DELETE        | `200 OK`      | `404 Not Found`                     |

---

## 📊 JOINs — Visual Guide

For a detailed explanation of the JOIN types with visual diagrams and step-by-step examples, check:

👉 **[JOINs-guia-visual.md](../JOINs-guia-visual.en.md)**

---

## 6) Simple JOIN (`Character` + `Planet`)

### ORM

```python
stmt = (
    select(Character.name, Planet.name.label("planet_name"))
    .join(Planet, Character.planet_id == Planet.id)
    .order_by(Character.name.asc())
)
rows = db.session.execute(stmt).all()
```

### Equivalent SQL

```sql
SELECT c.name, p.name AS planet_name
FROM characters c
JOIN planets p ON c.planet_id = p.id
ORDER BY c.name ASC;
```

---

## 7) Multiple JOIN with `LEFT JOIN`

Case: list users with their profile and favorite characters (if any).

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

### Equivalent SQL

```sql
SELECT u.username, up.bio, c.name AS favorite_character
FROM users u
JOIN user_profiles up ON up.user_id = u.id
LEFT JOIN favorites f ON f.user_id = u.id
LEFT JOIN characters c ON c.id = f.character_id
ORDER BY u.username ASC, c.name ASC;
```

---

## 8) Complex JOIN + aggregation (`GROUP BY` + `HAVING`)

Case: characters with at least `N` users who marked them as a favorite.

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

### Equivalent SQL

```sql
SELECT c.name, COUNT(f.user_id) AS total_users
FROM characters c
JOIN favorites f ON f.character_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(f.user_id) >= 1
ORDER BY total_users DESC, c.name ASC;
```

---

## 9) `N-N` JOIN (`Character` <-> `Film`)

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

### Equivalent SQL

```sql
SELECT f.title, c.name
FROM films f
JOIN character_films cf ON cf.film_id = f.id
JOIN characters c ON c.id = cf.character_id
WHERE f.title = 'A New Hope'
ORDER BY c.name ASC;
```

---

## 10) How to run the full demo

```bash
flask --app day_26/example_app.py db upgrade
python -m day_26.example_queries
```

The script runs inserts, an update, a select, a delete, and several joins.

---

## ✅ Step Checklist

- [ ] I inserted specific rows with the ORM.
- [ ] I updated a row using a condition on `id`.
- [ ] I selected data with simple filters.
- [ ] I deleted a specific row safely.
- [ ] I built at least 2 queries with joins.
- [ ] I built a query with aggregation and `HAVING`.
