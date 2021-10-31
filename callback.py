from aiohttp import web

from app import bot
from config import cb_confirm_token


async def callback_executor(request: web.Request):
    json = await request.json()

    if json.get("type") == "confirmation":
        return web.Response(body=cb_confirm_token)

    await bot.router.route(json, bot.api)
    return web.Response(body="ok")


app = web.Application()
app.router.add_route("POST", "/bot", callback_executor)

web.run_app(app, port=80)
