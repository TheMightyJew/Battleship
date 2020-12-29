"""
Purpose: a module represents class of a session message for the BattleShip game
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 29/12/2020
"""
from enum import Enum, auto
from Messages.baseMessage import BaseMessage


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

    def __init__(self, session_type, token, version):
        self.session_type = session_type
        self.token = token
        self.version = version

    def get_session_type(self):
        return self.session_type

    def get_token(self):
        return self.token

    def get_version(self):
        return self.version
