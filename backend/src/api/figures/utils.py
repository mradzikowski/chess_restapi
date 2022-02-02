from typing import List, Tuple


def list_available_moves_pawn(field: str, directions: List[Tuple]) -> None | List[str]:
    """
    Helper method to collect all available moves for pawn. If pawn is located on 2nd row
    on the board from the bottom, there is additional move by two squares

    :param field: field represented in string
    :param directions: possible directions for the figure
    :return: list of available moves for the current position
    """
    available_moves = []
    curr_row, curr_col = string_field_to_indexes(field=field)
    for direction in directions:
        pos_row = curr_row + direction[0]
        pos_col = curr_col + direction[1]
        if check_if_figure_in_board(row=pos_row, col=pos_col):
            available_moves.append(
                indexes_to_field(row_index=pos_row, col_index=pos_col),
            )
    if curr_row == 6:
        available_moves.append(
            indexes_to_field(row_index=curr_row - 2, col_index=curr_col),
        )
    return available_moves


def check_if_valid_move_pawn(
    curr_field: str,
    dest_field: str,
    directions: List[Tuple],
) -> bool:
    """
    Helper method to check if the desired move is valid for pawn

    :param curr_field: current position of figure
    :param dest_field: desired destination of figure
    :param directions: possible directions for the figure
    :return: True if is valid, False if not valid
    """
    available_moves = list_available_moves_pawn(field=curr_field, directions=directions)
    if dest_field in available_moves:
        return True
    return False


def list_available_moves_single_square(
    field: str,
    directions: List[Tuple],
) -> None | List[str]:
    """
    Helper method to collect all available moves for knight and king

    :param field: field represented in string
    :param directions: possible directions for the figure
    :return: list of available moves for the current position
    """
    available_moves = []
    curr_row, curr_col = string_field_to_indexes(field=field)
    for direction in directions:
        pos_row = curr_row + direction[0]
        pos_col = curr_col + direction[1]
        if check_if_figure_in_board(row=pos_row, col=pos_col):
            available_moves.append(
                indexes_to_field(row_index=pos_row, col_index=pos_col),
            )
    return available_moves


def check_if_valid_single_point_move(
    curr_field: str,
    dest_field: str,
    directions: List[Tuple],
) -> bool:
    """
    Helper method to check if the desired move is valid for knight and kind

    :param curr_field: current position of figure
    :param dest_field: desired destination of figure
    :param directions: possible directions for the figure
    :return: True if is valid, False if not valid
    """
    available_moves = list_available_moves_single_square(
        field=curr_field,
        directions=directions,
    )
    if dest_field in available_moves:
        return True
    return False


def list_available_moves_multiple_squares(
    field: str,
    directions: List[Tuple],
) -> None | List[str]:
    """
    Helper method to collect all available moves for bishop, rook and queen

    :param field: field represented in string
    :param directions: possible directions for the figure
    :return: list of available moves for the current position
    """
    available_moves = []
    curr_row, curr_col = string_field_to_indexes(field=field)
    for direction in directions:
        temp_row, temp_col = curr_row, curr_col
        while True:
            temp_row += direction[0]
            temp_col += direction[1]
            if check_if_figure_in_board(row=temp_row, col=temp_col):
                available_moves.append(
                    indexes_to_field(row_index=temp_row, col_index=temp_col),
                )
            else:
                break
    return available_moves


def check_if_valid_multiple_squares(
    curr_field: str,
    dest_field: str,
    directions: List[Tuple],
) -> bool:
    """
    Helper method to check if the desired move is valid for bishop, queen and rook

    :param curr_field: current position of figure
    :param dest_field: desired destination of figure
    :param directions: possible directions for the figure
    :return: True if is valid, False if not valid
    """
    available_moves = list_available_moves_multiple_squares(
        field=curr_field,
        directions=directions,
    )
    if dest_field in available_moves:
        return True
    return False


def check_if_figure_in_board(row: int, col: int) -> bool:
    """
    Helper method to check if the current position of figure is in board

    :param row: index of row
    :param col: index of column
    :return: True if valid, False if not valid
    """
    if 0 <= row < 8 and 0 <= col < 8:
        return True
    else:
        return False


def string_field_to_indexes(field: str) -> (int, int):
    """
    Helper method to change the string representation of position to indices

    :param field: current position on the board represented in string
    :return: indices of the current position
    """
    letters_to_numbers = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
    }
    letter = field[0]
    number = int(field[1])
    return 8 - number, letters_to_numbers[letter]


def indexes_to_field(row_index: int, col_index: int) -> str:
    """
    Helper method to represent x and y indices of current field in string

    :param row_index: index of row
    :param col_index: index of column
    :return: string representation of current field
    """
    numbers_to_letters = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
    }
    return numbers_to_letters[col_index] + str(8 - row_index)


def check_if_valid_field(field: str) -> bool:
    """
    Helper method to check if the passed field is valid

    :param field: str representation of field
    :return: True if valid, False if not valid
    """
    if not len(field) == 2:
        return False
    if not (ord("a") <= ord(field[0]) <= ord("h")):
        return False
    if not (ord("1") <= ord(field[1]) <= ord("8")):
        return False
    return True
