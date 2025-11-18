import asyncio  # noqa: F401

from aiogram.fsm.storage.redis import RedisStorage
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.bot.handlers.user import user
from app.bot.handlers.admin import admin
from app.config.settings import get_settings
from app.utils.redis import get_redis


async def main():
    settings = get_settings()
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
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
