from flask_restx import Api
from src.api.moves.views import moves_namespace

api = Api(version="1.0", title="API Chess Backend", doc="/doc")

api.add_namespace(moves_namespace, "/api/v1")
