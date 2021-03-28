from typing import Union, List

from models import Chat, ChatMessage
from .base import BaseRepository


class ChatRepository(BaseRepository):
    model = Chat

    async def get_by_peer(self, peer: int) -> [Chat, None]:
        return await self.get(peer=peer)


class MessageRepository(BaseRepository):
    model = ChatMessage

    async def get_messages(self, chat: Chat) -> Union[List[ChatMessage], List]:
        return await self.filter(chat=chat)
