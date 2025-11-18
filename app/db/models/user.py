from datetime import datetime
import asyncio  # noqa: F401

from sqlalchemy import func
from sqlalchemy import DateTime, BigInteger, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import expression

from app.db.models.base import Base


class User(Base):
    __tablename__ = "bot_user"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(String(32), nullable=True)
    is_admin: Mapped[bool] = mapped_column(default=expression.false())
    is_blocked: Mapped[bool] = mapped_column(default=expression.false())
    last_activity_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
