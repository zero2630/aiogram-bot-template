import asyncio  # noqa: F401

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from sqlalchemy import select, update
from aiogram.filters import Command, CommandStart

from keyboards import reply, inline
from other.database import async_session_maker
from other.models import User


router = Router()


@router.message(CommandStart())
async def command_start(message: Message, command: Command):

    await message.answer("start text", reply_markup=reply.main)
