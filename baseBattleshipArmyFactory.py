"""
Purpose: a module that represents interface for a factory for battleship's army
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""


class BaseBattleshipArmyFactory:
    """
    Interface for a factory for battleship's army
    """

    def create_army(self, battleships: list):
        """
        create an BattleshipArmy
        :param battleships: the battleship of the army
        :return BattleshipArmy: an valid army
        """
        raise NotImplementedError
