import asyncio  # noqa: F401
import random
from datetime import datetime, timedelta

from keyboards import inline
from bot import bot
from other.database import async_session_maker

async def cool_func():
    return None