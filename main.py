import asyncio  # noqa: F401
from datetime import datetime

from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy import update, select, insert

from app.bot.handlers.user import user
from app.bot.handlers.admin import admin

from bot import bot, dp
from app.db.database import async_session_maker
from app.db.models.models import User
from utils import utils


async def main():
    storage = RedisStorage.from_url("redis://localhost:6379/0")
    banned_storage = RedisStorage.from_url("redis://localhost:6379/1")
    dp.include_routers(
        user.router,
        admin.router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
