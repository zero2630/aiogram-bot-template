import asyncio  # noqa: F401

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from app.bot.keyboards import reply

router = Router()


@router.message(Command("admin"))
async def command_admin(message: Message):
    await message.answer(
        "admin mode",
        reply_markup=reply.get_admin_menu(),
    )
