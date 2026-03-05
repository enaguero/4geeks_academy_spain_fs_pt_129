import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///day26.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models after db init so Flask-Migrate can detect metadata.
    from day_26 import example_models  # noqa: F401

    @app.get("/health")
    def health():
        return {"status": "ok", "module": "day_26"}

    return app


app = create_app()
