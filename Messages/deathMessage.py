"""
Purpose: a module represents class of a death message for the BattleShip game
Author: Steven Danishevski
Created: 30/12/2020
Last edit: 30/12/2020
"""
from Messages.baseMessage import BaseMessage
from coordinate import Coordinate
from consts import BattleshipConsts, MessagesConsts

class DeathMessage(BaseMessage):
    """
    Class of a death message for the BattleShip game
    """

    def __init__(self, battleship_length=0, coordinate=None, direction=None):
        self.battleship_length = battleship_length
        self.coordinate = coordinate
        self.direction = direction

    def serialize(self):
        battleship_length_bytes = self.battleship_length.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        row_index_bytes = self.coordinate.row_index.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        col_index_bytes = self.coordinate.row_index.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        direction_bytes = self.direction.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        payload = battleship_length_bytes + row_index_bytes + col_index_bytes + direction_bytes
        message_code = MessagesConsts.DEATH
        return message_code + bytes(len(payload)) + payload

    def deserialize(self, bytes_rep):
        index = 0

        battleship_length = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH

        row_index = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH

        col_index = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH

        self.direction = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        self.battleship_length = battleship_length
        self.coordinate = Coordinate(row_index, col_index)
