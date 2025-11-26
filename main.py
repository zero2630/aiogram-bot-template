import asyncio  # noqa: F401
import logging

from aiogram.fsm.storage.redis import RedisStorage
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers.user import user, create_note, watch_note
from app.bot.handlers.admin import admin
from app.config.settings import get_settings
from app.utils.redis import get_redis
from app.bot.middlewares import logging_middleware, spam_middleware, activity_middleware


def setup_logging(level: str = "INFO"):
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


async def main():
    settings = get_settings()
    setup_logging()
    redis_client = await get_redis()

    storage = RedisStorage(redis=redis_client)

    bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher(storage=storage)

    dp.include_routers(
        user.router,
        admin.router,
        create_note.router,
        watch_note.router,
    )
    dp.update.middleware(logging_middleware.LoggingMiddleware())
    dp.update.middleware(activity_middleware.ActivityMiddleware(storage.redis))
    dp.message.middleware(spam_middleware.SpamMiddleware(storage))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
