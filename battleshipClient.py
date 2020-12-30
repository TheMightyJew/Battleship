"""
Purpose: a module that represents the client for the battleship game
Author: Steven Danishevski
Created: 30/12/2020
Last edit: 30/12/2020
"""
import socket
from Messages.sessionMessage import SessionMessage, SessionType
from consts import BattleshipConsts, MessagesConsts
from random import randrange
from battleshipErrors import InvalidMessageFlow


class BattleshipClient:
    """
    The client for the battleship game
    """
    def __init__(self, battleship_army):
        self.battleshipArmy = battleship_army
        self.token = None

    def play_as_listener(self, port):
        """
        play as the second player in the game, waiting for someone to approach me
        :param port: the port im listening on
        """
        pass

    def play_as_approacher(self, ip, port):
        """
        Play as the first player in the game, approaching a second player
        :param ip: the ip address of the second player
        :param port: the port address that the second player listens on
        """
        self.token = randrange(BattleshipConsts.MAX_INT_FROM_4_BYTES)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        connect_message = SessionMessage(SessionType.Connect, self.token, BattleshipConsts.CURRENT_VERSION).serialize()
        s.send(connect_message)
        data = s.recv(MessagesConsts.MESSAGE_CODE_SIZE)
        if data != MessagesConsts.NO and data != MessagesConsts.YES:
            raise InvalidMessageFlow(data)
        elif data == MessagesConsts.NO:
            exit()
        """
        need to continue the code 
        """
        s.close()
