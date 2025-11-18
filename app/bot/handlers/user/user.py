import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from app.bot.keyboards import reply, inline
from app.services import user

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, command: Command):
    await user.create_user(message.from_user.id)
    await message.answer(
        "Стартовый текст",
        reply_markup=reply.get_main_menu(),
    )


@router.message(F.text == "настройки")
async def settings(message: Message):
    await message.answer(
    "настройки",
    reply_markup=inline.get_user_settings_kb(message.from_user.id)
    )

