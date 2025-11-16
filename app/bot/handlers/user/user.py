import asyncio  # noqa: F401

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from app.bot.keyboards import reply

router = Router()


@router.message(CommandStart())
async def command_start(message: Message, command: Command):

    await message.answer("start text", reply_markup=reply.main)
