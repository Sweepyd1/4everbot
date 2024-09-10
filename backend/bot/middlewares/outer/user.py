from typing import Any, Awaitable, Callable, Optional, cast
from loguru import logger
from aiogram import BaseMiddleware
from aiogram.types import Chat, TelegramObject, User


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any]
    ) -> Optional[Any]:

        aiogram_user: Optional[User] = data.get("event_from_user")
        chat: Optional[Chat] = data.get("event_chat")
        if aiogram_user is None or chat is None or aiogram_user.is_bot:
            # Prevents the bot itself from being added to the database
            # when accepting chat_join_request and receiving chat_member.
            return await handler(event, data)

        user = ...  # Получаем данные о юзере

        if user is None:
            logger.info("New user in database: %s (%d)", aiogram_user.full_name, aiogram_user.id)

        data["user"] = user
        return await handler(event, data)
