"""
Purpose: a module that contains consts for the Battleship project
Author: Steven Danishevski
Created: 29/12/2020
Last edit: 30/12/2020
"""


class BattleshipConsts:
    """
    Consts for the battleships objects
    """
    CURRENT_VERSION = 1
    MIN_COORDINATE = 1
    MAX_COORDINATE = 10
    BYTES_REP_LENGTH = 2
    MAX_INT_FROM_4_BYTES = 65535
    BYTES_WRITING_STYLE = 'little'


class ErrorsConsts:
    NOT_STRAIGHT_COORDINATES_ERROR_MSG = 'All battleship\'s coordinates must be align in a straight line'
    NOT_POSITIVE_SHIP_LENGTH_ERROR_MSG = 'Battleship length must be higher than 0'
    INVALID_COORDINATE_ERROR_MSG_PART1 = 'Coordinates must be values in the range:'
    INVALID_COORDINATE_ERROR_MSG_PART2 = 'The following coordinate is invalid:'
    INVALID_BATTLESHIP_POS_MSG = 'The battleships must be at least 2 coordinates far away from each other'
    INVALID_BATTLESHIP_STRUCT_MSG = 'The battleships structure does not match the structure of the given army'
    INVALID_MESSAGE_CODE_MSG = 'The following message code is invalid:'
    INVALID_MESSAGE_PAYLOAD_MSG1 = 'For the message code:'
    INVALID_MESSAGE_PAYLOAD_MSG2 = 'the following message code is invalid:'
    INVALID_MESSAGE_FLOW_MSG = 'This is invalid message flow to receive now a message with the code:'


class MessagesConsts:
    MESSAGE_CODE_SIZE = 3
    CONNECT_SESSION = bytes('\x00' * 3)
    YES = bytes('\x00' * 2 + '\x01')
    NO = bytes('\x00' * 2 + '\x02')
    CONTINUE_SESSION = bytes('\x00' * 2 + '\x03')
    ATTACK = bytes('\x00' * 2 + '\x04')
    ERROR = bytes('\x00' * 2 + '\x05')
    DISCONNECT_SESSION = bytes('\x00' * 2 + '\x06')
    READY = bytes('\x00' * 2 + '\x07')
    DEATH = bytes('\x00' * 2 + '\x08')
    KEEP_ALIVE = bytes('\x00' * 2 + '\x09')
