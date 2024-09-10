import contextlib
import uvicorn
from aiogram.utils.callback_answer import CallbackAnswerMiddleware

from bot.handlers import router
from bot.middlewares import UserMiddleware
from routes import main_router
from core import loader
from typing import AsyncIterator
from loguru import logger

from core.loader import app, dp, bot, cfg


async def on_startup():
    ##==> Include routers
    ##################################
    dp.include_routers(router)

    ##==> Setup inner middlewares
    ################################################################
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    ##==> Setup outer middlewares
    ####################################################
    dp.update.outer_middleware(UserMiddleware())

    logger.add(
        "../logs/log_{time}.log",
        level="DEBUG",
        format="{time} | {level} | {module}:{function}:{line} | {message}",
        rotation="500 KB",
        compression="zip"
    )
    logger.success("Сервер успешно запущен!")
    await bot.set_webhook(
        cfg.webhook.full_url,
        allowed_updates=dp.resolve_used_update_types(),
        secret_token=cfg.webhook.secret_token.get_secret_value(),
    )


async def on_shutdown():
    if not cfg.webhook.reset:
        return
    if await bot.delete_webhook():
        logger.info("Dropped main bot webhook.")
    else:
        logger.error("Failed to drop main bot webhook.")
    await bot.session.close()


@contextlib.asynccontextmanager
async def lifespan(_) -> AsyncIterator[None]:
    await on_startup()
    yield
    await on_shutdown()


if __name__ == "__main__":
    app.router.lifespan_context = lifespan

    ##==> Include routes to the FastAPI
    ###################################
    app.include_router(main_router)

    uvicorn.run(loader.app, host=cfg.webhook.host, port=cfg.webhook.port)
