from flask import Flask
from flask_restx import Api

from HomeWork_18_Architecture.config import Config
from HomeWork_18_Architecture.setup_db import db
from HomeWork_18_Architecture.application.views.movies import movie_ns
from HomeWork_18_Architecture.application import genre_ns
from HomeWork_18_Architecture.application import director_ns


# Функция создания основного объекта app
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    configure_app(app)
    return app


# Подключение настроек/расширений
def configure_app(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    return app


if __name__ == '__main__':
    app = create_app(Config())
    app.run(debug=True)
