import asyncio  # noqa: F401

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from app.bot.keyboards import reply
from app.services import user

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, command: Command):
    await user.create_user(message.from_user.id)
    await message.answer(
        "Стартовый текст",
        reply_markup=reply.get_main_menu(),
    )
