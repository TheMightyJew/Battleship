"""
Purpose: a module represents class produces objects of messages
Author: Steven Danishevski
Created: 30/12/2020
Last edit: 30/12/2020
"""
from consts import MessagesConsts, ErrorsConsts
from battleshipErrors import InvalidMessageError
from Messages.answerMessage import AnswerMessage
from Messages.attackMessage import AttackMessage
from Messages.deathMessage import DeathMessage
from Messages.errorMessage import ErrorMessage
from Messages.sessionMessage import SessionMessage


class MessageFactory:
    """
    Class produces objects of messages
    """

    def create_message(self, message_code, payload):
        if message_code in MessageFactory.CREATORS.keys():
            message = MessageFactory.CREATORS[message_code]()
            try:
                message.deserialize(payload)
            except:
                raise InvalidMessageError(
                    f'{ErrorsConsts.INVALID_MESSAGE_PAYLOAD_MSG1} {str(message_code)} {ErrorsConsts.INVALID_MESSAGE_PAYLOAD_MSG2} {str(payload)}')
            return message
        raise InvalidMessageError(f'{ErrorsConsts.INVALID_MESSAGE_CODE_MSG} {str(message_code)}')

    CREATORS = {MessagesConsts.CONNECT_SESSION: SessionMessage, MessagesConsts.YES: AnswerMessage,
                MessagesConsts.NO: AnswerMessage, MessagesConsts.CONTINUE_SESSION: SessionMessage,
                MessagesConsts.ATTACK: AttackMessage, MessagesConsts.ERROR: ErrorMessage,
                MessagesConsts.DISCONNECT_SESSION: SessionMessage, MessagesConsts.READY: SessionMessage,
                MessagesConsts.DEATH: DeathMessage, MessagesConsts.KEEP_ALIVE: SessionMessage}
