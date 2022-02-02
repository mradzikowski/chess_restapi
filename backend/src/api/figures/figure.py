from abc import ABC, abstractmethod
from typing import List, Union

from src.api.figures.utils import (
    check_if_valid_field,
    check_if_valid_move_pawn,
    check_if_valid_multiple_squares,
    check_if_valid_single_point_move,
    list_available_moves_multiple_squares,
    list_available_moves_pawn,
    list_available_moves_single_square,
)


class Figure(ABC):
    """Abstract class of figure"""

    @abstractmethod
    def __init__(self, field: str):
        pass

    @abstractmethod
    def list_available_moves(self):
        """Abstract method to retrieve available moves"""
        pass

    @abstractmethod
    def validate_move(self, dest_field: str):
        """Abstract method to check if the desired move is valid"""
        pass


class King(Figure):
    """Class of King's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the king

        :return: list of available moves
        """
        return list_available_moves_single_square(
            field=self.field,
            directions=self.directions,
        )

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for king

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_single_point_move(
            curr_field=self.field,
            dest_field=dest_field,
        )


class Rook(Figure):
    """Class of Rook's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the rook

        :return: list of available moves
        """
        return list_available_moves_multiple_squares(
            field=self.field,
            directions=self.directions,
        )

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for rook

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_multiple_squares(
            curr_field=self.field,
            dest_field=dest_field,
        )


class Bishop(Figure):
    """Class of Bishop's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the bishop

        :return: list of available moves
        """
        return list_available_moves_multiple_squares(
            field=self.field,
            directions=self.directions,
        )

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for bishop

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_multiple_squares(
            curr_field=self.field,
            dest_field=dest_field,
        )


class Queen(Figure):
    """Class of Queen's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
        ]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the queen

        :return: list of available moves
        """
        return list_available_moves_multiple_squares(
            field=self.field,
            directions=self.directions,
        )

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for queen

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_multiple_squares(
            curr_field=self.field,
            dest_field=dest_field,
        )


class Knight(Figure):
    """Class of Knight's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [
            (1, 2),
            (2, -1),
            (1, -2),
            (2, 1),
            (-1, -2),
            (-2, -1),
            (-2, 1),
            (-1, 2),
        ]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the knight

        :return: list of available moves
        """
        return list_available_moves_single_square(
            field=self.field,
            directions=self.directions,
        )

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for knight

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_single_point_move(
            curr_field=self.field,
            dest_field=dest_field,
        )


class Pawn(Figure):
    """Class of Pawn's figure that implements figure's methods"""

    def __init__(self, field: str):
        if not check_if_valid_field(field):
            raise ValueError("Field does not exist.")
        self.field = field
        self.directions = [(-1, 0)]

    def list_available_moves(self) -> Union[None, List[str]]:
        """
        Class method to retrieve available moves for the pawn

        :return: list of available moves
        """
        return list_available_moves_pawn(field=self.field, directions=self.directions)

    def validate_move(self, dest_field: str) -> bool:
        """
        Check if the desired move is valid for pawn

        :param dest_field: destination field in string
        :return: True if valid, False if not valid
        """
        return check_if_valid_move_pawn(
            curr_field=self.field,
            dest_field=dest_field,
            directions=self.directions,
        )
