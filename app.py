from vkbottle import load_blueprints_from_package
from vkbottle.bot import Bot

from middlewares import middlewares
import config

bot = Bot(config.token, config.group_id)

for bp in load_blueprints_from_package("blueprints"):
    bp.load(bot)
    
for md in middlewares:
    bot.labeler.message_view.register_middleware(md())

if __name__ == "__main__":
    bot.run_forever()
