from app.core.config import variables
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

print("Creating Asynchronous SQLAlchemy Engine...")
engine = create_async_engine(variables.DB_URL, echo=True)
SessionLocal = async_sessionmaker(bind=engine,autoflush=False, expire_on_commit=False)
print("Succesfully Started Local Session To: ", variables.DB_URL)


# We do not have any common attributes across tables for now.
class Base(DeclarativeBase):
    pass

# Initialising Database models
from app.models import *
