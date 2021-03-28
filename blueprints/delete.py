from vkbottle.bot import Blueprint, Message
from repositories import ChatRepo, MessageRepo

bp = Blueprint("DelMsgBlueprint")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text=".delete messages")
async def delete_message_command(message: Message):
    chat = await ChatRepo.get_by_peer(message.peer_id)
    await MessageRepo.delete(
        await MessageRepo.get_messages(chat))
    return "База сообщений очищена"


