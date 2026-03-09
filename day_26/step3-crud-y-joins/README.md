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

## 📖 ¿Qué es CRUD?

**CRUD** es el acrónimo de las cuatro operaciones fundamentales que puedes realizar sobre datos persistentes:

| Letra | Operación | Significado                         |
| ----- | --------- | ----------------------------------- |
| **C** | Create    | Crear nuevos registros              |
| **R** | Read      | Leer/consultar registros existentes |
| **U** | Update    | Modificar registros existentes      |
| **D** | Delete    | Eliminar registros                  |

### ¿Por qué es importante?

Prácticamente **toda aplicación que almacena datos** necesita estas cuatro operaciones. Ya sea una red social, un e-commerce, o un blog — todas crean, leen, actualizan y eliminan datos.

### 🔗 La conexión CRUD → SQL → HTTP → ORM

Lo interesante es que CRUD se mapea directamente a:

- **SQL**: Los comandos que la base de datos entiende
- **HTTP**: Los métodos que las REST APIs usan
- **ORM**: Los métodos de Python/SQLAlchemy

| CRUD       | SQL           | HTTP Method     | SQLAlchemy ORM                    | Endpoint típico               |
| ---------- | ------------- | --------------- | --------------------------------- | ----------------------------- |
| **Create** | `INSERT INTO` | `POST`          | `db.session.add(obj)`             | `POST /users`                 |
| **Read**   | `SELECT`      | `GET`           | `db.session.execute(select(...))` | `GET /users` o `GET /users/1` |
| **Update** | `UPDATE`      | `PUT` / `PATCH` | `obj.campo = nuevo_valor`         | `PUT /users/1`                |
| **Delete** | `DELETE`      | `DELETE`        | `db.session.delete(obj)`          | `DELETE /users/1`             |

> 💡 **Insight clave**: Cuando construyes una REST API con Flask, cada endpoint típicamente ejecuta una de estas operaciones CRUD en la base de datos.

---

## 1) Base de ejemplo

Modelos y app usados en este step:

- `day_26/example_app.py`
- `day_26/example_models.py`
- `day_26/example_queries.py`

---

## 2) CREATE — INSERT de filas específicas

### ¿Qué hace?

Crea uno o más registros nuevos en la base de datos.

### ¿Cuándo usarlo?

- Registro de nuevos usuarios
- Crear posts, comentarios, productos
- Cualquier formulario de "crear nuevo X"

### En REST API

Típicamente se invoca con `POST /recurso` y el body contiene los datos del nuevo registro.

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

## 3) UPDATE — Modificar fila específica

### ¿Qué hace?

Modifica los valores de uno o más campos de un registro existente.

### ¿Cuándo usarlo?

- Editar perfil de usuario
- Cambiar estado de un pedido
- Actualizar cualquier dato existente

### En REST API

Típicamente se invoca con `PUT /recurso/{id}` o `PATCH /recurso/{id}`.

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

## 4) READ — SELECT simple y filtrado

### ¿Qué hace?

Consulta y recupera registros de la base de datos, opcionalmente con filtros.

### ¿Cuándo usarlo?

- Mostrar lista de usuarios
- Buscar un producto por ID
- Filtrar posts por categoría
- Cualquier pantalla que muestre datos

### En REST API

Típicamente se invoca con `GET /recurso` (listar) o `GET /recurso/{id}` (obtener uno).

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

## 5) DELETE — Eliminar fila específica

### ¿Qué hace?

Elimina permanentemente un registro de la base de datos.

### ¿Cuándo usarlo?

- Eliminar cuenta de usuario
- Borrar un post o comentario
- Remover un producto del catálogo

### En REST API

Típicamente se invoca con `DELETE /recurso/{id}`.

### ⚠️ Precaución

El DELETE es permanente. En producción, considera usar "soft delete" (marcar como eliminado con un campo `deleted_at` en lugar de borrar físicamente).

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

## 🌐 CRUD en Flask: Endpoints REST completos

Aquí tienes ejemplos de cómo se ve cada operación CRUD implementada como endpoint Flask:

### Setup previo

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

    # Validación básica
    if not body or 'email' not in body or 'username' not in body:
        return jsonify({"error": "email y username son requeridos"}), 400

    # Verificar si ya existe
    existing = db.session.execute(
        select(User).where(User.email == body['email'])
    ).scalar_one_or_none()

    if existing:
        return jsonify({"error": "El email ya está registrado"}), 400

    # Crear usuario
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
        return jsonify({"error": "Usuario no encontrado"}), 404

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
        return jsonify({"error": "Usuario no encontrado"}), 404

    body = request.get_json()

    # Actualizar campos si vienen en el body
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
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Usuario eliminado correctamente"}), 200
```

### Resumen de códigos de estado HTTP

| Operación     | Éxito         | Error común                         |
| ------------- | ------------- | ----------------------------------- |
| POST (Create) | `201 Created` | `400 Bad Request` (datos inválidos) |
| GET (Read)    | `200 OK`      | `404 Not Found`                     |
| PUT (Update)  | `200 OK`      | `404 Not Found`                     |
| DELETE        | `200 OK`      | `404 Not Found`                     |

---

## 📊 JOINs — Guía Visual

Para una explicación detallada de los tipos de JOIN con diagramas visuales y ejemplos paso a paso, consulta:

👉 **[JOINs-guia-visual.md](../JOINs-guia-visual.md)**

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
