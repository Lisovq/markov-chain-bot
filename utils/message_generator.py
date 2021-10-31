from typing import Union
import string
import mc

from config import settings
from database import Chat, ChatMessage


class generate:
    def gen(peer: int) -> Union[str, None]:
        messages = ChatMessage.select(ChatMessage.text).where(
            ChatMessage.peer_id == peer
        )
        return generate.sentence(messages)

    def create(peer: int, text_characters: list) -> None:
        for text in map(restrict, text_charapters):
            ChatMessage.create(message=text, chat_id=peer)
        
    def sentence(messages: tuple[ChatMessage]) -> Union[str, None]:
        generator = mc.StringGenerator([message.strip() for mess in messages])
        return generator.generate_string(
            5, settings.words_generate, settings.syntaz
        ) or None


def restrict(text: str) -> str:
    text = text.replace("\n", ", ")
    if text[-1] in string.punctuation:
        text = text[:-1]
    
    return text
