from bot_app import init_bot_app
from config import CALLBACK_CONFIRMATION_TOKEN

from aiohttp import web
from ujson import loads

bot = init_bot_app()


async def callback_executor(request: web.Request):
    json = await request.json(loads=loads)

    if json.get("type") == "confirmation":
        return web.Response(body=CALLBACK_CONFIRMATION_TOKEN)

    await bot.router.route(json, bot.api)
    return web.Response(body="ok")


app = web.Application()
app.router.add_route("POST", "/bot", callback_executor)

web.run_app(app, port=80)
