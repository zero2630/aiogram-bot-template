import asyncio  # noqa: F401

from sqlalchemy import select, update, join
from sqlalchemy.dialects.postgresql import insert


from app.db.models.user import User
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker



async def get_user_settings(tg_id: int):
    async with async_session_maker() as session:
        stmt = select(UserSettings).join(User, UserSettings.user == User.id).where(User.tg_id == tg_id)
        res = (await session.execute(stmt)).scalar_one_or_none()

        return res


async def change_lang(tg_id: int):
        async with async_session_maker() as session:
            stmt = (
            select(UserSettings)
            .join(User, UserSettings.user == User.id)
            .where(User.tg_id == tg_id)
            )

            settings = (await session.execute(stmt)).scalar_one_or_none()

            stmt = (
                update(UserSettings)
                .where(UserSettings.id == settings.id)
                .values(is_ru=(not settings.is_ru))
            )

            await session.execute(stmt)
            await session.commit()


async def change_notif(tg_id: int):
        async with async_session_maker() as session:
            stmt = (
            select(UserSettings)
            .join(User, UserSettings.user == User.id)
            .where(User.tg_id == tg_id)
            )

            settings = (await session.execute(stmt)).scalar_one_or_none()

            stmt = (
                update(UserSettings)
                .where(UserSettings.id == settings.id)
                .values(is_notificate=(not settings.is_notificate))
            )

            await session.execute(stmt)
            await session.commit()
