"""
Purpose: a module that represents a factory that creates olympus battleships army
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from consts import ErrorsConsts
from baseBattleshipArmyFactory import BaseBattleshipArmyFactory
from battleshipErrors import InvalidBattleshipsPosError
from battleshipsArmy import BattleshipsArmy


def is_ships_far_enough(battleships):
    """
    checks if ship are at least two coordinates away from each other
    :param battleships: the battleships to examine
    :return bool: true if ships are far enough from each other, false otherwise
    """
    for ship_index in range(len(battleships)):
        for other_ship_index in range(ship_index + 1, len(battleships)):
            for coordinate in battleships[ship_index].get_coordinates():
                for other_coordinate in battleships[other_ship_index].get_coordinates():
                    if max(abs(coordinate.row_index - other_coordinate.row_index),
                           abs(coordinate.col_index - other_coordinate.col_index)) < 2:
                        return False
    return True


class OlympusBattleshipArmyFactory(BaseBattleshipArmyFactory):
    """
    Creates an olympus type battleships army
    """
    BATTLESHIPS_STRUCT = {2: 1, 3: 2, 4: 1, 5: 1}

    def create_army(self, battleships: list):
        """
        creates an battleships army by a given battleships
        :param battleships: the given battleships
        :return BattleshipArmy: the army
        :raise InvalidBattleshipsPosError: if the does not stand the olympus conditions
        """
        if not is_ships_far_enough(battleships):
            raise InvalidBattleshipsPosError(ErrorsConsts.INVALID_BATTLESHIP_POS_MSG)
        if not self.is_valid_battleships_structure(battleships):
            raise InvalidBattleshipsPosError(ErrorsConsts.INVALID_BATTLESHIP_STRUCT_MSG)
        return BattleshipsArmy(battleships)

    def is_valid_battleships_structure(self, battleships):
        """
        checks if the battleships answer the olympus condition
        :param battleships: the battleships to examine
        :return bool: true if answer the olympus structure
        """
        if sum(OlympusBattleshipArmyFactory.BATTLESHIPS_STRUCT.values()) != len(battleships):
            return False
        for ship_size, quantity in OlympusBattleshipArmyFactory.BATTLESHIPS_STRUCT.items():
            if quantity != sum(map(lambda battleship: battleship.get_size() == ship_size, battleships)):
                return False
        return True
