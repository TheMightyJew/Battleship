"""
Purpose: a module represents class of a answer message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from Messages.baseMessage import BaseMessage


class AnswerMessage(BaseMessage):
    """
    Class of a answer message for the BattleShip game
    """

    def __init__(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer
