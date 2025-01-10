
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from typing import AsyncGenerator
SQLALCHAMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session