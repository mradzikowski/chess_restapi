import os

from flask import Flask


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from src.api import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
