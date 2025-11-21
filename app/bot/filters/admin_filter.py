from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.config.settings import get_settings


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        settings = get_settings()
        return message.from_user.id in settings.ADMINS