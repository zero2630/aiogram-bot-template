import asyncio  # noqa: F401

from sqlalchemy import select, update, func
from sqlalchemy.dialects.postgresql import insert


from app.db.models.note import Note
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker


async def create_note(title, text):
    async with async_session_maker() as session:
        stmt = insert(Note).values(title=title, text=text)
        res = await session.execute(stmt)
        await session.commit()
        inserted_id = res.scalar_one_or_none()

        return inserted_id


async def get_note(offset):
    async with async_session_maker() as session:
        stmt = (
            select(Note)
            .order_by(Note.id)
            .limit(1)
            .offset((offset))
        )
        res = (await session.execute(stmt)).scalar_one_or_none()

        return res

async def get_notes_amount():
    async with async_session_maker() as session:
        stmt = select(func.count()).select_from(Note)
        result = (await session.execute(stmt)).scalar_one()
        return result
