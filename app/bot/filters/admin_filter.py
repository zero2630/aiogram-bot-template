from aiogram.filters import BaseFilter
from aiogram.types import Message
from sqlalchemy import select

from app.config.settings import get_settings
from app.db.database import async_session_maker
from app.db.models.user import User


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with async_session_maker() as session:
            settings = get_settings()
            tg_id = message.from_user.id

            stmt = select(User.tg_id).where(User.is_admin == True)
            res = (await session.scalars(stmt)).all()
            print(res)

            return tg_id == settings.OWNER_ID or tg_id in res