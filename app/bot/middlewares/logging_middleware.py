import logging
import time
from typing import Any, Callable, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update, Message, CallbackQuery


logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:

        start_time = time.monotonic()

        user_id = None
        chat_id = None
        text = None
        event_type = type(event).__name__

        
        if event.message:
            chat_id = event.message.chat.id
            user_id = event.message.from_user.id
            text = event.message.text or event.message.caption
        elif event.callback_query:
            chat_id = event.callback_query.message.chat.id
            user_id = event.callback_query.message.from_user.id
            text = event.callback_query.data

        logger.info(
            "Incoming update: type=%s user_id=%s chat_id=%s text=%r",
            event_type,
            user_id,
            chat_id,
            text,
        )

        try:
            result = await handler(event, data)
        except Exception as e:
            elapsed = time.monotonic() - start_time
            logger.exception(
                "Error while handling update: type=%s user_id=%s chat_id=%s "
                "elapsed=%.3fs error=%r",
                event_type,
                user_id,
                chat_id,
                elapsed,
                e,
            )
            raise

        elapsed = time.monotonic() - start_time
        logger.info(
            "Handled update successfully: type=%s user_id=%s chat_id=%s elapsed=%.3fs",
            event_type,
            user_id,
            chat_id,
            elapsed,
        )

        return result
