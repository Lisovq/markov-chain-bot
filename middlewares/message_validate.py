import re
from vkbottle.dispatch import BaseMiddleware

from config import settings
from config import patterns

from utils import randomize
from utils import generate


class ValidateMessageMiddleware(BaseMiddleware):
    async def pre(self, message) -> bool:
        return all([
            message.peer_id > 2e9,
            message.from_id > 0,
            message.text
        ])

    async def post(self, message, view, responses, handlers):
        if responses or len(message.text) > MAX_LEN_MESSAGE:
            return

        text = re.sub(patterns.link, "ССЫЛКА УДАЛЕНА", message.text)
        generate.create(message.peer_id, text.split("\n\n"))

        if settings.random_send and randomize():
            await message.answer(generate_message(message.peer_id))
