from vkbottle.bot import Blueprint, Message
from database import ChatMessages

bp = Blueprint("DeleteMessagesBlueprint")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text=".delete msgs")
async def delete_chat_messages(message: Message):
    ChatMessages.where(ChatMessages.peer_id == message.peer_id).delete()
    return "База сообщений очищена"
