from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from fastapi import FastAPI

from .config import AppConfig, CommonConfig, PostgresConfig, WebhookConfig

cfg: AppConfig = AppConfig(
    common=CommonConfig(),
    postgres=PostgresConfig(),
    webhook=WebhookConfig(),
)

app: FastAPI = FastAPI()

bot: Bot = Bot(
    token=cfg.common.bot_token.get_secret_value(),
    parse_mode=ParseMode.HTML
)

dp: Dispatcher = Dispatcher(
    name="main_dispatcher",
    server=MemoryStorage(),
    config=cfg,
)