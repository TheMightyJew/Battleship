"""
Purpose: a module that contains errors (exceptions) for the Battleship project
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from consts import ErrorsConsts


class BaseBattleshipError(Exception):
    """
    Base error for the Battleship project
    """

    def __init__(self, error_msg):
        super(BaseBattleshipError, self).__init__(error_msg)


class InvalidCoordinateError(BaseBattleshipError):
    """
    Error for invalid coordinate
    """

    def __init__(self, invalid_coordinate, valid_range):
        error_msg = f'{ErrorsConsts.INVALID_COORDINATE_ERROR_MSG_PART1} {valid_range}. {ErrorsConsts.INVALID_COORDINATE_ERROR_MSG_PART1} {invalid_coordinate}. '
        super(InvalidCoordinateError, self).__init__(error_msg)


class InvalidBattleshipCoordinatesError(BaseBattleshipError):
    """
    Error for invalid battleship coordinates
    """

    def __init__(self, error_msg):
        super(InvalidBattleshipCoordinatesError, self).__init__(error_msg)


class InvalidBattleshipsPosError(BaseBattleshipError):
    """
    Error for invalid battleship position
    """

    def __init__(self, error_msg):
        super(InvalidBattleshipsPosError, self).__init__(error_msg)
