"""
Purpose: a module represents class of a session message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from enum import Enum, auto
from Messages.baseMessage import BaseMessage
from consts import BattleshipConsts, MessagesConsts


class SessionType(Enum):
    Connect = auto,
    Continue = auto,
    Disconnect = auto,
    Ready = auto,
    KeepAlive = auto


class SessionMessage(BaseMessage):
    """
    Class of a session message for the BattleShip game
    """

    def __init__(self, session_type=None, token=None, version=None):
        self.session_type = session_type
        self.token = token
        self.version = version

    def serialize(self):
        session_type_bytes = self.session_type.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        token_bytes = self.token.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        version_bytes = self.version.to_bytes(BattleshipConsts.BYTES_REP_LENGTH, BattleshipConsts.BYTES_WRITING_STYLE)
        payload = session_type_bytes + token_bytes + version_bytes
        message_code = MessagesConsts.DEATH
        return message_code + bytes(len(payload)) + payload

    def deserialize(self, bytes_rep):
        index = 0

        self.session_type = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH

        self.token = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH

        self.version = int.from_bytes(bytes_rep[index:index + BattleshipConsts.BYTES_REP_LENGTH], BattleshipConsts.BYTES_WRITING_STYLE)
        index += BattleshipConsts.BYTES_REP_LENGTH