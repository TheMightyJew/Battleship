"""
Purpose: a module represents class of a answer message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 30/12/2020
"""
from Messages.baseMessage import BaseMessage
from consts import MessagesConsts


class AnswerMessage(BaseMessage):
    """
    Class of a answer message for the BattleShip game
    """
    message_codes = {True: MessagesConsts.YES, False: MessagesConsts.NO}

    def __init__(self, answer=False):
        self.answer = answer

    def serialize(self):
        payload = bytes(self.answer)
        message_code = AnswerMessage.message_codes[self.answer]
        return message_code + bytes(len(payload)) + payload

    def deserialize(self, bytes_representation):
        self.answer = bool(bytes_representation)
