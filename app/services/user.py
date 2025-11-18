import asyncio  # noqa: F401

from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert


from app.db.models.user import User
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker



async def create_user(tg_id: int):

    async with async_session_maker() as session:
        stmt = insert(User).values(tg_id=tg_id).on_conflict_do_nothing().returning(User.id)
        res = await session.execute(stmt)
        inserted_id = res.scalar_one_or_none()
        print(inserted_id)

        if inserted_id:
            stmt = insert(UserSettings).values(user=inserted_id).on_conflict_do_nothing()
            await session.execute(stmt)
            await session.commit()

