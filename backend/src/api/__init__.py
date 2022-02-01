from flask_restx import Api
from src.api.figure.views import figure_namespace

api = Api(version="1.0", title="API Chess Backend", doc="/doc")

api.add_namespace(figure_namespace, "/api/v1")
