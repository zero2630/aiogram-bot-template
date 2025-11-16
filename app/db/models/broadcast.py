from datetime import datetime
from typing import Any, Dict
import asyncio  # noqa: F401

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import String, Text, DateTime, BigInteger
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.models.base import Base


class Broadcast(Base):
    __tablename__ = "broadcast"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    created_by: Mapped[int] = mapped_column(ForeignKey("bot_user.id"), ondelete="CASCADE")
    text: Mapped[str] = mapped_column(Text)
    keyboard: Mapped[Dict[str, Any]] = mapped_column(JSONB, nullable=True) # структура inline клавиатуры
    segment: Mapped[Dict[str, Any]] = mapped_column(JSONB, nullable=True) # критерии сегментации
    sent_count Mapped[int] = mapped_column(server_default="0")
    error_count Mapped[int] = mapped_column(server_default="0")

