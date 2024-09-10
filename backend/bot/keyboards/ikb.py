from core.loader import cfg
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

fill_quest = InlineKeyboardMarkup(
    row_width=1,
    inline_keyboard=[
        [InlineKeyboardButton(text='Заполнить анкету', web_app=WebAppInfo(url=cfg.webhook.base_url + "/memory_page"))]
])
