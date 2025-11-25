# app/bot/middlewares/activity_middleware.py

import logging
from typing import Any, Awaitable, Callable, Dict, Optional

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from redis.asyncio import Redis

from app.services.user import update_user_activity

logger = logging.getLogger(__name__)


class ActivityMiddleware(BaseMiddleware):

    def __init__(
        self,
        redis: Redis,
        min_interval_seconds: int = 60,
        prefix: str = "user:last_activity",
    ) -> None:
        super().__init__()
        self.redis = redis
        self.min_interval_seconds = min_interval_seconds
        self.prefix = prefix

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        tg_user = None

        if event.message:
            tg_user = event.message.from_user.id
        elif event.callback_query:
            tg_user = event.callback_query.message.from_user.id

        if tg_user is not None:
            key = f"{self.prefix}:{tg_user}"

            try:
                updated = await self.redis.set(
                    key,
                    "1",
                    ex=self.min_interval_seconds,
                    nx=True,
                )

                if updated:
                    await update_user_activity(tg_user)
            except Exception:
                logger.exception(
                    "Failed to update user activity for tg_id=%s", tg_user
                )

        return await handler(event, data)
