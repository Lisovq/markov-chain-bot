from vkbottle.dispatch import BaseMiddleware

from config import RANDOM_SEND, MAX_LEN_MESSAGE
from use_cases import LINK_PATTERN, create_messages, generate_message

from re import findall
import random


class ValidateMessageMiddleware(BaseMiddleware):
    """ Validate message and load to db """

    async def pre(self, message):
        return message.from_id > 0 and message.peer_id > 2e9

    async def post(self, message, view, responses, handlers):
        if message.peer_id < 2e9 or responses or not message.text:
            return

        if len(message.text) < MAX_LEN_MESSAGE and not findall(LINK_PATTERN, message.text):
            await create_messages(message.peer_id, message.text.split("\n\n"))

        if RANDOM_SEND and random.randint(0, 33) == 24:
            await message.answer(await generate_message(message.peer_id))
