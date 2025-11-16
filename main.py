import asyncio  # noqa: F401

from app.bot.handlers.user import user
from app.bot.handlers.admin import admin

from bot import bot, dp


async def main():
    dp.include_routers(
        user.router,
        admin.router,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
