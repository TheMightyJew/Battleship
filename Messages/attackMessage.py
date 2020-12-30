"""
Purpose: a module represents class of a attack message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 30/12/2020
"""
from Messages.baseMessage import BaseMessage
from coordinate import Coordinate
from consts import BattleshipConsts, MessagesConsts

class AttackMessage(BaseMessage):
    """
    Class of a attack message for the BattleShip game
    """

    def __init__(self, coordinate=Coordinate(0, 0)):
        self.coordinate = coordinate

    def serialize(self):
        row_index_bytes = self.coordinate.row_index.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        col_index_bytes = self.coordinate.row_index.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        payload = row_index_bytes + col_index_bytes
        message_code = MessagesConsts.ATTACK
        return message_code + bytes(len(payload)) + payload

    def deserialize(self, bytes_rep):
        row_index = int.from_bytes(bytes_rep[:BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        col_index = int.from_bytes(bytes_rep[BattleshipConsts.BYTES_REP_LENGTH:], BattleshipConsts.BYTES_WRITING_STYLE)
        self.coordinate = Coordinate(row_index, col_index)
