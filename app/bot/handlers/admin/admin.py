import asyncio  # noqa: F401

from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(Command("admin"))
async def command_admin(message: Message):
    await message.answer("admin mode")
