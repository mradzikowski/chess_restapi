from typing import Union

from src.api.figures.figure import Bishop, King, Knight, Pawn, Queen, Rook

chess_figures = {"rook", "king", "queen", "pawn", "knight", "bishop"}


def check_if_valid_chess_figure(chess_figure: str) -> bool:
    """
    Helper method to check if the chess figure name is valid

    :param chess_figure: string representation of the chess figure
    :return: True if valid, False if not
    """
    return chess_figure in chess_figures


def get_figure_by_name(
    chess_figure: str,
    curr_field: str,
) -> Union[Pawn, King, Queen, Knight, Bishop, Rook]:
    """
    Helper method to retrieve the object by name and create

    :param chess_figure: string representation of the chess figure
    :param curr_field: current field of the object
    :return: The object of figure based on the chess figure name
    """
    if chess_figure == "pawn":
        return Pawn(field=curr_field)
    elif chess_figure == "king":
        return King(field=curr_field)
    elif chess_figure == "queen":
        return Queen(field=curr_field)
    elif chess_figure == "knight":
        return Knight(field=curr_field)
    elif chess_figure == "bishop":
        return Bishop(field=curr_field)
    else:
        return Rook(field=curr_field)
