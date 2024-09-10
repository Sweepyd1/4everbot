from typing import Any, Final
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import ikb

router: Final[Router] = Router(name=__name__)


@router.message(CommandStart())
async def start_command(message: Message, user: dict) -> Any:
    return message.answer(
        text=f"Приветствую, {message.from_user.full_name}!\nЗаполните страницу памяти.",
        reply_markup=ikb.fill_quest,
    )
