from vkbottle.bot import Blueprint, Message
from use_cases.message_generator import generate_message

bp = Blueprint("MsgGenBlueprint")
bp.labeler.vbml_ignore_case = True


@bp.on.chat_message(text=".gen")
async def generate_command(message: Message):
    return (
        await generate_message(message.peer_id) or
        "Collected text in this Chat small for generate sentence"
    )
