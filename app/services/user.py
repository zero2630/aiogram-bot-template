import asyncio  # noqa: F401
from datetime import datetime, timedelta

from sqlalchemy import select, update, func
from sqlalchemy.dialects.postgresql import insert

from app.db.models.user import User
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker



async def create_user(tg_id: int):
    async with async_session_maker() as session:
        stmt = insert(User).values(tg_id=tg_id).on_conflict_do_nothing().returning(User.id)
        res = await session.execute(stmt)
        inserted_id = res.scalar_one_or_none()

        if inserted_id:
            stmt = insert(UserSettings).values(user=inserted_id).on_conflict_do_nothing()
            await session.execute(stmt)
            await session.commit()


async def update_user_activity(tg_id: int):
    async with async_session_maker() as session:
        stmt = update(User).values(last_activity_at=datetime.utcnow()).where(User.tg_id == tg_id)
        await session.execute(stmt)
        await session.commit()


async def get_users_amount():
    async with async_session_maker() as session:
        stmt = func.count(User.id)
        res = (await session.execute(stmt)).scalar()
        return res

async def get_users_amount_banned():
    async with async_session_maker() as session:
        stmt = select(func.count(User.id)).where(User.is_blocked == True)
        res = (await session.scalar(stmt))
        return res

async def get_users_active(duration: timedelta):
    async with async_session_maker() as session:
        now = datetime.utcnow()
        time_ago = now - duration
        stmt = select(func.count(User.id)).where(User.last_activity_at >= time_ago)
        res = (await session.scalar(stmt))
        return res


async def get_users_page(offset):
    async with async_session_maker() as session:
        stmt = (
            select(Page)
            .order_by(Page.id)
            .limit(2)
            .offset((offset))
        )
        res = (await session.execute(stmt)).scalar_one_or_none()

        return res
