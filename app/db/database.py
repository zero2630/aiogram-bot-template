import asyncio  # noqa: F401
import sys

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
    from app.db.models.base import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
    from app.db.models.base import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def recreate_tables():
    from app.db.models.base import Base

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def main():
    args = sys.argv
    if len(args) == 2:
        param = args[1]
        if param == "create":
            create_tables()
        elif param == "drop":
            drop_tables()
        elif param == "recreate":
            recreate_tables()



if __name__ == "__main__":
    asyncio.run(create_tables())
