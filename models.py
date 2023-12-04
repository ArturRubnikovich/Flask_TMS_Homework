import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

dsn = "sqlite:///lesson18.db"
engine = create_engine(dsn, echo=True)
session = sessionmaker(bind=engine, autoflush=False)


class Base(DeclarativeBase):
    pass


class Note(Base):
    __tablename__ = "notes"
    uuid = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(256))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)
