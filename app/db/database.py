import asyncio  # noqa: F401

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import get_settings


settings = get_settings()

DATABASE_URL = (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@"
                f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

engine = create_async_engine(DATABASE_URL, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    from models import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())
