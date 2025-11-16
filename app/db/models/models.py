from datetime import datetime
import asyncio  # noqa: F401

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import String, Text, DateTime, BigInteger
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "bot_user"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

