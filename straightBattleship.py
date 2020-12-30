"""
Purpose: a module that represents a class for a straight battleship
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from consts import ErrorsConsts
from coordinate import Coordinate
from baseBattleship import BaseBattleship
from battleshipErrors import InvalidBattleshipCoordinatesError
from enum import Enum, auto


class Direction(Enum):
    Down = auto,
    Up = auto,
    Right = auto,
    Left = auto


def is_straight_coordinates(coordinates: list):
    """
    check if all coordinates align in a straight line
    :param coordinates: the coordinates to examine
    :return bool: true if align in straight line, false otherwise
    """
    row_delta = 0
    col_delta = 0
    coordinates = sorted(coordinates)
    for index in range(1, len(coordinates)):
        row_delta += abs(coordinates[index].row_index - coordinates[index - 1].row_index)
        col_delta += abs(coordinates[index].col_index - coordinates[index - 1].col_index)
        if 0 < min(row_delta, col_delta) or max(row_delta, col_delta) != index:
            return False
    return True


class StraightBattleship(BaseBattleship):
    """
    class for straight battleship
    """

    def __init__(self, battleship_length, coordinate: Coordinate, direction: Direction):
        """
        Initiate straight battleship while checking the coordinates are valid
        :param battleship_length: the length of the ship
        :param coordinate: the head coordinate of the ship
        :param direction: the direction of the ship starting from the head
        """
        self.battleship_length = battleship_length
        self.head_coordinate = coordinate
        self.direction = direction
        self.coordinates = None
        coordinates = [coordinate]
        for counter in range(battleship_length):
            if direction is Direction.Down:
                coordinates.append(Coordinate(coordinate.row_index + counter, coordinate.col_index))
            elif direction is Direction.Up:
                coordinates.append(Coordinate(coordinate.row_index - counter, coordinate.col_index))
            elif direction is Direction.Right:
                coordinates.append(Coordinate(coordinate.row_index, coordinate.col_index + counter))
            elif direction is Direction.Left:
                coordinates.append(Coordinate(coordinate.row_index, coordinate.col_index - counter))
        self.set_coordinates(coordinates)

    def set_coordinates(self, coordinates: list):
        """
        Initiate straight battleship while checking the coordinates are valid
        :param coordinates: the coordinates of the ship
        :raise InvalidBattleshipCoordinatesError: if the coordinates are invalid
        """
        if len(coordinates) <= 0:
            raise InvalidBattleshipCoordinatesError(ErrorsConsts.NOT_POSITIVE_SHIP_LENGTH_ERROR_MSG)
        if is_straight_coordinates(coordinates):
            raise InvalidBattleshipCoordinatesError(ErrorsConsts.NOT_STRAIGHT_COORDINATES_ERROR_MSG)
        self.coordinates = {coordinate: True for coordinate in coordinates}

    def suffer_shot(self, coordinate: Coordinate):
        if coordinate not in self.coordinates.keys():
            return False
        else:
            self.coordinates[coordinate] = False
            return True

    def is_alive(self):
        return any(self.coordinates.values())

    def get_coordinates(self):
        return list(self.coordinates.keys())

    def get_size(self):
        return self.battleship_length
