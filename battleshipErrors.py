"""
Purpose: a module that contains errors (exceptions) for the Battleship project
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""


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
    ERROR_MSG_PART1 = 'Coordinates must be values in the range:'
    ERROR_MSG_PART2 = 'The following coordinate is invalid:'

    def __init__(self, invalid_coordinate, valid_range):
        error_msg = f'{InvalidCoordinateError.ERROR_MSG_PART1} {valid_range}. {InvalidCoordinateError.ERROR_MSG_PART2} {invalid_coordinate}. '
        super(InvalidCoordinateError, self).__init__(error_msg)
