"""
Purpose: a module represents an interface of a message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""


class BaseMessage:
    """
    Interface of a message for the BattleShip game
    """

    def serialize(self):
        """
        change the message representation to byte code
        :return bytes: byte code
        """
        raise NotImplementedError()

    def deserialize(self, bytes_rep):
        """
        sets the variables from bytes representation
        :param bytes_rep: the representation of the variables
        """
        raise NotImplementedError()
