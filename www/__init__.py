from flask import Flask, render_template
from flask_compress import Compress
from flask_cors import CORS

from config import config

compress = Compress()


def create_app(config_name):
    app = Flask(__name__)
    compress.init_app(app)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    CORS(app, supports_credentials=True)

    @app.route("/")
    def welcome():
        return render_template("welcome.jinja2")

    from .views import api

    api.init_app(app)

    return app
