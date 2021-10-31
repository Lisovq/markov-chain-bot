from vkbottle.bot import Blueprint, Message
from utils import generate

bp = Blueprint("GenerateBlueprint")
bp.labeler.vbml_ignore_case = True


@bp.on.chat_message(text=".generate")
async def generate_command(message: Message):
    return (
        generate.gen(message.peer_id) or
        "Collected text in this Chat small for generate sentence"
    )
