from flask import Flask


def register_blueprints(app):
    from src.api.v1 import web_v1
    app.register_blueprint(web_v1, url_prefix='/v1')


def register_plugins(app):
    from src.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def init_config(app):
    app.config.from_object("src.config.setting")
    app.config.from_object("src.config.secure")


def create_app():
    # __name__ is a special Python variable that gets as value the string "__main__" when you’re executing the script.
    app = Flask(__name__)
    init_config(app)
    register_blueprints(app)
    register_plugins(app)

    return app
