import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
# from logger import log

load_dotenv(verbose=True)

DB_USER = os.getenv("DB_USER", None)
DB_PASSWORD = os.getenv("DB_PASSWORD", None)
DB_HOST = os.getenv("DB_HOST", None)
DB_PORT = os.getenv("DB_PORT", None)
DB_NAME = os.getenv("DB_NAME", None)
DB_SECRET = os.getenv("DB_SECRET", None)


async def get_db():
    engine = create_async_engine(
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        future=True,
        echo=True,
    )
    async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    return async_session_factory()


async def close_db(e=None):
    pass
    # print("close_db requested")
    # if db is not None:
    #     log.info("Closing db connection")
    #     await db.close()
    # else:
    #     log.info("db connection already closed. No action taken.")
