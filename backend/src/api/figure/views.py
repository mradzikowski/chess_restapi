from flask_restx import Namespace, Resource

figure_namespace = Namespace("figure")


class Move(Resource):
    pass


class MovesList(Resource):
    pass


figure_namespace.add_resource(Move)
figure_namespace.add_resource(MovesList)
