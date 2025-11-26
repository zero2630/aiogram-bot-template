from datetime import datetime
import asyncio  # noqa: F401

from sqlalchemy import func
from sqlalchemy import DateTime, BigInteger, String, Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression

from app.db.models.base import Base


class Note(Base):
    __tablename__ = "note"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    title: Mapped[str] = mapped_column(String(50))
    text: Mapped[str] = mapped_column(Text)