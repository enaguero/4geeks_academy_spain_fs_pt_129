from sqlalchemy import func, select

from day_26.example_app import app, db
from day_26.example_models import Character, Favorite, Film, Planet, User, UserProfile


def insert_seed_data():
    tatooine = Planet(name="Tatooine", climate="arid")
    alderaan = Planet(name="Alderaan", climate="temperate")

    luke = Character(name="Luke Skywalker", species="Human", homeworld=tatooine)
    leia = Character(name="Leia Organa", species="Human", homeworld=alderaan)

    ep4 = Film(title="A New Hope", release_year=1977)
    ep5 = Film(title="The Empire Strikes Back", release_year=1980)

    luke.films.extend([ep4, ep5])
    leia.films.extend([ep4, ep5])

    user = User(email="ana@example.com", username="ana_dev")
    user.profile = UserProfile(bio="StarWars fan", avatar_url="https://img.example/avatar.png")
    user.favorites.append(Favorite(character=luke, note="Best Jedi arc"))

    db.session.add_all([tatooine, alderaan, luke, leia, ep4, ep5, user])
    db.session.commit()


def insert_specific_user(email, username, bio):
    new_user = User(email=email, username=username)
    new_profile = UserProfile(bio=bio)  
    new_user.profile = new_profile
    db.session.add(new_user)
    db.session.commit()
    return new_user.id

def update_user_email(user_id, new_email):
    user = db.session.get(User, user_id)
    # Select * from users where id = user_id
    if user is None:
        return False

    user.email = new_email
    db.session.commit()
    return True


def select_user_by_username(username):
    stmt = select(User).where(User.username == username)
    return db.session.execute(stmt).scalar_one_or_none()


def delete_character_by_name(name):
    character = db.session.execute(
        select(Character).where(Character.name == name)
    ).scalar_one_or_none()
    if character is None:
        return False

    db.session.delete(character)
    db.session.commit()
    return True


def join_characters_with_homeworld():
    stmt = (
        select(Character.name, Planet.name.label("planet_name"))
        .join(Planet, Character.planet_id == Planet.id)
        .order_by(Character.name.asc())
    )
    return db.session.execute(stmt).all()


def join_users_profiles_favorites():
    stmt = (
        select(User.username, UserProfile.bio, Character.name.label("favorite_character"))
        .join(UserProfile, UserProfile.user_id == User.id)
        .outerjoin(Favorite, Favorite.user_id == User.id)
        .outerjoin(Character, Character.id == Favorite.character_id)
        .order_by(User.username.asc(), Character.name.asc())
    )
    return db.session.execute(stmt).all()


def top_characters_by_favorites(min_users=1):
    stmt = (
        select(Character.name, func.count(Favorite.user_id).label("total_users"))
        .join(Favorite, Favorite.character_id == Character.id)
        .group_by(Character.id, Character.name)
        .having(func.count(Favorite.user_id) >= min_users)
        .order_by(func.count(Favorite.user_id).desc(), Character.name.asc())
    )
    return db.session.execute(stmt).all()


def characters_by_film_title(film_title):
    stmt = (
        select(Film.title, Character.name)
        .join(Film.characters)
        .where(Film.title == film_title)
        .order_by(Character.name.asc())
    )
    return db.session.execute(stmt).all()


def demo():
    if db.session.execute(select(User.id)).first() is None:
        insert_seed_data()

    new_user_id = insert_specific_user(
        email="luis@example.com",
        username="luis_data",
        bio="Me interesan migraciones y joins",
    )
    update_user_email(new_user_id, "luis.orm@example.com")

    _ = select_user_by_username("luis_data")
    _ = delete_character_by_name("Leia Organa")

    print("JOIN simple: Character + Planet")
    for row in join_characters_with_homeworld():
        print(row)

    print("\nJOIN con LEFT JOIN: User + Profile + Favorites")
    for row in join_users_profiles_favorites():
        print(row)

    print("\nJOIN + GROUP BY + HAVING")
    for row in top_characters_by_favorites(min_users=1):
        print(row)

    print("\nJOIN N-N Character <-> Film")
    for row in characters_by_film_title("A New Hope"):
        print(row)


if __name__ == "__main__":
    with app.app_context():
        demo()
