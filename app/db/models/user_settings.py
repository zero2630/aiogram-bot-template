from datetime import datetime
import asyncio  # noqa: F401

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import DateTime, BigInteger, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import expression

from app.db.models.base import Base


class UserSettings(Base):
    __tablename__ = "user_settings"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    user: Mapped[int] = mapped_column(ForeignKey("bot_user.id", ondelete="CASCADE"), unique=True)
    is_ru: Mapped[bool] = mapped_column(default=expression.true())
    is_notificate: Mapped[bool] = mapped_column(default=expression.true())
