"""
Purpose: a module to represent a coordinate in a battleship game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from consts import BattleshipConsts
from battleshipErrors import InvalidCoordinateError


def is_valid_point(point:int):
    """
    Checks if a point is a valid point
    :param point: the point to observe
    :return: true if valid, false othewise
    """
    return BattleshipConsts.MIN_COORDINATE <= point <= BattleshipConsts.MAX_COORDINATE


class Coordinate:
    """
    Represent a coordinate in a battleship game
    """

    def __init__(self, row_index:int, col_index:int):
        """
        Initiate a coordinate if valid
        :param row_index: the row index value for the coordinate
        :param col_index: the column index value for the coordinate
        :raise: InvalidCoordinateError if invalid coordinate
        """
        if not is_valid_point(row_index) or not is_valid_point(col_index):
            raise InvalidCoordinateError((row_index, col_index),
                                         (BattleshipConsts.MIN_COORDINATE, BattleshipConsts.MAX_COORDINATE))
        self.row_index = row_index
        self.col_index = col_index
