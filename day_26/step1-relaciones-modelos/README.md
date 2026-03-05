# Step 1: Relaciones entre modelos (`1-1`, `1-N`, `N-N`)

## 🎯 Objetivo

Modelar relaciones reales entre entidades usando SQLAlchemy para preparar Instagram/StarWars.

---

## 1) Relación `1-1` (uno a uno)

Caso: un `User` tiene un único `UserProfile`.

```python
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    profile = db.relationship(
        "UserProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

class UserProfile(db.Model):
    __tablename__ = "user_profiles"
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255))
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False,
    )

    user = db.relationship("User", back_populates="profile")
```

Puntos clave:

- `unique=True` en `user_id` evita múltiples perfiles para un mismo usuario.
- `uselist=False` hace que `user.profile` sea un objeto, no una lista.

---

## 2) Relación `1-N` (uno a muchos)

Caso: un `Planet` tiene muchos `Character`.

```python
class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    characters = db.relationship("Character", back_populates="homeworld")

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)

    homeworld = db.relationship("Planet", back_populates="characters")
```

Puntos clave:

- La FK vive en el lado “muchos” (`Character.planet_id`).
- Un planeta puede tener N personajes, cada personaje un solo planeta.

---

## 3) Relación `N-N` (muchos a muchos)

Caso: un `Character` aparece en muchas `Film`, y una `Film` tiene muchos `Character`.

```python
character_films = db.Table(
    "character_films",
    db.Column("character_id", db.Integer, db.ForeignKey("characters.id"), primary_key=True),
    db.Column("film_id", db.Integer, db.ForeignKey("films.id"), primary_key=True),
)

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    films = db.relationship(
        "Film",
        secondary=character_films,
        back_populates="characters",
    )

class Film(db.Model):
    __tablename__ = "films"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)

    characters = db.relationship(
        "Character",
        secondary=character_films,
        back_populates="films",
    )
```

Puntos clave:

- Necesitas tabla puente (`character_films`).
- PK compuesta evita duplicados del mismo par (`character_id`, `film_id`).

---

## 4) ¿Dónde ver un ejemplo completo?

Revisa:

- `day_26/example_models.py`

Incluye las tres relaciones principales y una relación adicional `User <-> Character` mediante `Favorite`.

---

## ✅ Checklist de este step

- [ ] Definí al menos una relación `1-1`.
- [ ] Definí al menos una relación `1-N`.
- [ ] Definí al menos una relación `N-N`.
- [ ] Entiendo en qué tabla vive cada `ForeignKey`.
