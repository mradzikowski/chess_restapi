from flask_restx import Namespace, Resource

moves_namespace = Namespace("figure")


class Move(Resource):
    pass


class MovesList(Resource):
    pass


moves_namespace.add_resource(Move)
moves_namespace.add_resource(MovesList)
