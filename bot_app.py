from vkbottle.bot import Bot
from vkbottle import load_blueprints_from_package

from use_cases.db import db_create_models
from middlewares import middlewares
from config import BOT_TOKEN, GROUP_ID


def init_bot_app():
    db_create_models()
    bot = Bot(BOT_TOKEN, GROUP_ID)

    for md in middlewares:
        bot.labeler.message_view.register_middleware(md())

    for bp in load_blueprints_from_package("blueprints"):
        bp.load(bot)

    return bot
