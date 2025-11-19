import asyncio  # noqa: F401

from sqlalchemy import select, update, func
from sqlalchemy.dialects.postgresql import insert


from app.db.models.page import Page
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker


async def create_page(title, text):
    async with async_session_maker() as session:
        stmt = insert(Page).values(title=title, text=text)
        res = await session.execute(stmt)
        await session.commit()
        inserted_id = res.scalar_one_or_none()

        return inserted_id


async def get_page(offset):
    async with async_session_maker() as session:
        stmt = (
            select(Page)
            .order_by(Page.id)
            .limit(1)
            .offset((offset))
        )
        res = (await session.execute(stmt)).scalar_one_or_none()

        return res

async def get_pages_amount():
    async with async_session_maker() as session:
        stmt = select(func.count()).select_from(Page)
        result = (await session.execute(stmt)).scalar_one()
        return result
