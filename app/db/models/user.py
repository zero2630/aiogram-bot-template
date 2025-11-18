from datetime import datetime
import asyncio  # noqa: F401

from sqlalchemy import func
from sqlalchemy import DateTime, BigInteger, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.models.base import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(32))
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    is_admin: Mapped[bool] = mapped_column(default="false")
    is_blocked: Mapped[bool] = mapped_column(default="false")
    last_activity_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
