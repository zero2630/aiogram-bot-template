import asyncio  # noqa: F401

from sqlalchemy import select, update, func
from sqlalchemy.dialects.postgresql import insert
from aiogram import Bot


from app.db.models.user import User
from app.db.models.user_settings import UserSettings
from app.db.database import async_session_maker
from app.bot.keyboards import inline



async def create_and_send_broadcast(text: str, bot: Bot):
    async with async_session_maker() as session:
        offset = 0
        sent = 0
        sent_success = 0
        sent_error = 0
        chunk_size = 1

        stmt_count = select(func.count(User.id))
        total_users =  await session.scalar(stmt_count) or 0

        chunk_size = chunk_size if total_users >= chunk_size else total_users

        while sent < total_users:

            stmt = select(User).where(User.is_blocked == False)
            stmt = stmt.order_by(User.id).offset(offset).limit(chunk_size)
            res = (await session.execute(stmt)).all()
            res = [item[0] for item in res]

            for user in res:
                await bot.send_message(user.tg_id, text, reply_markup=inline.get_broadcast_received_kb())
                await asyncio.sleep(0.05)

            sent += len(res)
            offset += len(res)
            

# 1. получение id по чанкам
# 2. рассылка id из чанка
# 3. обработка ошибок