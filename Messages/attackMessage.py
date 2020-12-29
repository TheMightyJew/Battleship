"""
Purpose: a module represents class of a attack message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from Messages.baseMessage import BaseMessage


class AttackMessage(BaseMessage):
    """
    Class of a attack message for the BattleShip game
    """

    def __init__(self, coordinate):
        self.coordinate = coordinate

    def get_coordinate(self):
        return self.coordinate
