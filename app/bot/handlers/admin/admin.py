import asyncio  # noqa: F401
import hashlib

from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.deep_linking import create_start_link
from sqlalchemy import insert, select, update

from app.bot.keyboards import reply
from app.bot.states import states
from app.db.models.models import User
from app.db.database import async_session_maker
from app.bot.keyboards import inline
from bot import bot


router = Router()

@router.message(Command("admin"))
async def command_admin(message: Message):
        await message.answer("admin mode")

