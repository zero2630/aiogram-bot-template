from typing import Callable, Any, Dict, Awaitable
import asyncio  # noqa: F401
import logging

from aiogram.types import TelegramObject, Message
from aiogram.enums.content_type import ContentType

import html


logger = logging.getLogger(__name__)


class SpamMiddleware:
    def __init__(self, storage):
        self.storage = storage

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ):
        new_event = event
        limit = 3
        ttl = 3
        user_id = event.from_user.id

        text = ""
        if event.content_type == ContentType.TEXT:
            new_event = event.model_copy(update={"text": html.escape(event.text)})
            text = new_event.text
        elif event.content_type == ContentType.PHOTO:
            if event.caption:
                new_event = event.model_copy(
                    update={"caption": html.escape(event.caption)}
                )
                text = new_event.caption

        if len(text) > 1000:
            await event.answer("Слишком большой текст сообщения")
            logger.info(
                "Large text triggered: user_id=%s",
                user_id,
            )
            return None

        await self.storage.redis.incr(user_id)
        count = int(await self.storage.redis.get(user_id))
        current_ttl = await self.storage.redis.ttl(user_id)
        print(await self.storage.redis.ttl(user_id), await self.storage.redis.get(user_id))
        if count == 1 or current_ttl == -1:
            await self.storage.redis.expire(user_id, ttl)
            return await handler(new_event, data)

        elif count > limit:
            await event.answer(
                "Слишком частые сообщения. Попробуйте чуть позже"
            )
            logger.info(
                "Antispam triggered: user_id=%s",
                user_id,
            )
            return None

        return await handler(new_event, data)
