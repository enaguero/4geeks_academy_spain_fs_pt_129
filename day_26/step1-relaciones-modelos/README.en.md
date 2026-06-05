[🇪🇸 Español](README.md) | 🇬🇧 **English**

# Step 1: Relationships between models (`1-1`, `1-N`, `N-N`)

## 🎯 Goal

Model real-world relationships between entities using SQLAlchemy to prepare for Instagram/StarWars.

---

## 1) `1-1` relationship (one to one)

Case: a `User` has a single `UserProfile`.

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

Key points:

- `unique=True` on `user_id` prevents multiple profiles for the same user.
- `uselist=False` makes `user.profile` a single object instead of a list.

---

## 2) `1-N` relationship (one to many)

Case: a `Planet` has many `Character`s.

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

Key points:

- The FK lives on the "many" side (`Character.planet_id`).
- One planet can have N characters; each character has only one planet.

---

## 3) `N-N` relationship (many to many)

Case: a `Character` appears in many `Film`s, and a `Film` has many `Character`s.

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

Key points:

- You need a junction table (`character_films`).
- The composite PK prevents duplicates of the same pair (`character_id`, `film_id`).

---

## 4) Where to see a complete example?

Check:

- `day_26/example_models.py`

It includes the three main relationships plus an additional `User <-> Character` relationship through `Favorite`.

---

## ✅ Step Checklist

- [ ] I defined at least one `1-1` relationship.
- [ ] I defined at least one `1-N` relationship.
- [ ] I defined at least one `N-N` relationship.
- [ ] I understand which table each `ForeignKey` lives in.
