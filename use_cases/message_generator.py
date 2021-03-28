from typing import Tuple

from config import USUAL_SYNTAX
from models import ChatMessage
from repositories import MessageRepo, ChatRepo

import string
import mc


# text formatter
def restrict(text) -> str:
    text = text.replace("\n", ", ")
    return text[:-1] if text[-1] in string.punctuation else text


async def create_messages(peer: int, text_charapters: list) -> None:
    chat = await ChatRepo.get_or_create(peer=peer)
    for text in map(restrict, text_charapters):
        await MessageRepo.create(message=text, chat=chat)


async def generate_sentence(messages: Tuple[ChatMessage]) -> str:
    gen_object = mc.StringGenerator([mess.message.strip() for mess in messages])
    generated = gen_object.generate_string(
        5, mc.validators.words_count(1, 20), USUAL_SYNTAX
    ) or None

    return generated


async def generate_message(peer: int) -> str:
    chat = await ChatRepo.get_by_peer(peer)
    messages = await MessageRepo.get_messages(chat)
    return await generate_sentence(messages)
