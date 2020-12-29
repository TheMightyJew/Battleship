"""
Purpose: a module that represents a class of battleships army
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""


class BattleshipsArmy:
    """
    Class of battleships army
    """

    def __init__(self, battleships):
        self.battleships = battleships
        self.last_shot_destroyed = False

    def suffer_shot(self, coordinate):
        """
        the battleships army suffers a shot
        :param coordinate: the coordinates of the shot
        :return: true if shot hit, false otherwise
        """
        self.last_shot_destroyed = False
        for battleship in self.battleships:
            if battleship.is_alive() and battleship.suffer_shot(coordinate):
                if not battleship.is_alive():
                    self.last_shot_destroyed = True
                return True
        return False

    def is_alive(self):
        """
        checks if the army is alive, meaning not all battleships got destroyed
        :return bool: true if at least one battleship is still alive
        """
        return any(map(lambda battleship: battleship.is_alive(), self.battleships))
