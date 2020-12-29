"""
Purpose: a module that contains consts for the Battleship project
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""


class BattleshipConsts:
    """
    Consts for the battleships objects
    """
    MIN_COORDINATE = 1
    MAX_COORDINATE = 10


class ErrorsConsts:
    NOT_STRAIGHT_COORDINATES_ERROR_MSG = 'All battleship\' coordinates must be align in a straight line'
    INVALID_COORDINATE_ERROR_MSG_PART1 = 'Coordinates must be values in the range:'
    INVALID_COORDINATE_ERROR_MSG_PART2 = 'The following coordinate is invalid:'
    INVALID_BATTLESHIP_POS_MSG = 'The battleships must be at least 2 coordinates far away from each other'
    INVALID_BATTLESHIP_STRUCT_MSG = 'The battleships structure does not match the structure of the given army'
