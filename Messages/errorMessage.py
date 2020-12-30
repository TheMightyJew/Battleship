"""
Purpose: a module represents class of a error message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from Messages.baseMessage import BaseMessage
from consts import MessagesConsts


class ErrorMessage(BaseMessage):
    """
    Class of a error message for the BattleShip game
    """

    def __init__(self, error_code=None):
        self.error_code = error_code

    def serialize(self):
        payload = self.error_code.encode()
        message_code = MessagesConsts.ERROR
        return message_code + bytes(len(payload)) + payload

    def deserialize(self, bytes_rep):
        self.error_code = bytes_rep.decode()
