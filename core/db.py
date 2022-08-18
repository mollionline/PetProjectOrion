from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import databases
from sqlalchemy.ext.asyncio import create_async_engine


SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://master:secret@localhost:5433/master"

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
Base: DeclarativeMeta = declarative_base()