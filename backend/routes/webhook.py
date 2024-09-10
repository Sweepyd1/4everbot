from aiogram import types
from fastapi import Request
from fastapi.responses import Response
from fastapi.routing import APIRouter

from core.loader import cfg, dp, bot

router = APIRouter()


@router.post("/webhook", status_code=200)
async def webhook(request: Request, update: types.Update):
    secret_key = request.headers.get("X-Telegram-Bot-Api-Secret-Token", None)

    if secret_key != cfg.webhook.secret_token.get_secret_value():
        return Response(status_code=200)

    await dp._process_update(bot=bot, update=update)
