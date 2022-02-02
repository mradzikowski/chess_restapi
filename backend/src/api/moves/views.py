from flask_restx import Namespace, Resource, fields
from src.api.moves.utils import check_if_valid_chess_figure, get_figure_by_name

moves_namespace = Namespace("figure")

move_validity_fields = moves_namespace.model(
    "Move Validity",
    {
        "figure": fields.String,
        "move": fields.String,
        "error": fields.String,
        "currentField": fields.String,
        "destField": fields.String,
    },
)

available_moves_fields = moves_namespace.model(
    "Available Moves",
    {
        "availableMoves": fields.List(fields.String),
        "error": fields.String,
        "figure": fields.String,
        "currentField": fields.String,
    },
)


class ValidChessMove(Resource):
    def get(self, chess_figure: str, curr_field: str, dest_field: str):
        response_object = {
            "figure": chess_figure,
            "currentField": curr_field,
            "destField": dest_field,
            "error": "null",
            "move": "invalid",
        }

        if not check_if_valid_chess_figure(chess_figure=chess_figure):
            response_object[
                "error"
            ] = f"Chess figure - {chess_figure} - does not exist."
            return response_object, 404

        try:
            figure = get_figure_by_name(
                chess_figure=chess_figure,
                curr_field=curr_field,
            )
        except ValueError:
            response_object["error"] = "Field does not exist."
            return response_object, 409

        if not figure.validate_move(dest_field=dest_field):
            response_object["error"] = "Current move is not permitted."

        response_object["move"] = "valid"
        return response_object, 200


class ValidChessMovesList(Resource):
    def get(self, chess_figure: str, curr_field: str):
        response_object = {
            "figure": chess_figure,
            "currentField": curr_field,
            "error": "null",
            "availableMoves": [],
        }

        if not check_if_valid_chess_figure(chess_figure=chess_figure):
            response_object[
                "error"
            ] = f"Chess figure - {chess_figure} - does not exist."
            return response_object, 404

        try:
            figure = get_figure_by_name(
                chess_figure=chess_figure,
                curr_field=curr_field,
            )
        except ValueError:
            response_object["error"] = "Field does not exist."
            return response_object, 409

        available_moves = figure.list_available_moves()
        response_object["availableMoves"] = available_moves
        return response_object, 200


moves_namespace.add_resource(
    ValidChessMove,
    "/<string:chess_figure>/<string:curr_field>/<string:dest_field>",
)
moves_namespace.add_resource(
    ValidChessMovesList,
    "/<string:chess_figure>/<string:curr_field>",
)
