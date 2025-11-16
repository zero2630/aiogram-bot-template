import asyncio  # noqa: F401
import random
from datetime import datetime, timedelta

from app.bot.keyboards import inline
from bot import bot
from app.db.database import async_session_maker

async def cool_func():
    return None