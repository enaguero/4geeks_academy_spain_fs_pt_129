from datetime import datetime

from day_26.example_app import db

character_films = db.Table(
    "character_films",
    db.Column("character_id", db.Integer, db.ForeignKey("characters.id"), primary_key=True),
    db.Column("film_id", db.Integer, db.ForeignKey("films.id"), primary_key=True),
)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # 1-1 relation with UserProfile
    profile = db.relationship(
        "UserProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    # N-N via association object Favorite
    favorites = db.relationship(
        "Favorite",
        back_populates="user",
        cascade="all, delete-orphan",
    )


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255), nullable=True)
    avatar_url = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)

    user = db.relationship("User", back_populates="profile")


class Planet(db.Model):
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120), nullable=True)

    # 1-N: one planet has many characters
    characters = db.relationship("Character", back_populates="homeworld")


class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(120), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)

    # N-1 side from Character to Planet
    homeworld = db.relationship("Planet", back_populates="characters")

    # N-N with Film via association table
    films = db.relationship(
        "Film",
        secondary=character_films,
        back_populates="characters",
    )

    # N-N with User via Favorite association object
    favorites = db.relationship(
        "Favorite",
        back_populates="character",
        cascade="all, delete-orphan",
    )


class Film(db.Model):
    __tablename__ = "films"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    release_year = db.Column(db.Integer, nullable=False)

    characters = db.relationship(
        "Character",
        secondary=character_films,
        back_populates="films",
    )


class Favorite(db.Model):
    __tablename__ = "favorites"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    note = db.Column(db.String(120), nullable=True)

    user = db.relationship("User", back_populates="favorites")
    character = db.relationship("Character", back_populates="favorites")
