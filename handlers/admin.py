import asyncio  # noqa: F401
import hashlib

from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.deep_linking import create_start_link
from sqlalchemy import insert, select, update

from keyboards import reply
from other import states
from other.models import User
from other.database import async_session_maker
from keyboards import inline
from bot import bot


router = Router()

@router.message(Command("admin"))
async def command_admin(message: Message):
        await message.answer("admin mode")

