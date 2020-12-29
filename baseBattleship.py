"""
Purpose: a module that represents an interface for a battleship
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from coordinate import Coordinate


class BaseBattleship:
    """
    Interface for a battleship
    """

    def suffer_shot(self, coordinate: Coordinate):
        """
        get a shot in a given coordinate
        :return bool: true if the shot hit the ship, false if missed
        """
        raise NotImplementedError()

    def is_alive(self):
        """
        checks if the ship alive, meaning not all parts got destroyed
        :return bool: true if at least one coordinate of the battleship is still alive
        """
        raise NotImplementedError()

    def get_coordinates(self):
        """
        returns the coordinates of the battleship
        :return list<Cordinates>: list of the coordinates
        """
        raise NotImplementedError()

    def get_size(self):
        """
        return the size of the battleship
        :return int: size of the battleship
        """
        raise NotImplementedError()
