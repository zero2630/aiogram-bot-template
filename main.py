import asyncio  # noqa: F401
from datetime import datetime

from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy import update, select, insert

from handlers import (
    user,
    admin
)
from bot import bot, dp
from other.database import async_session_maker
from other.models import User
from other import utils


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
