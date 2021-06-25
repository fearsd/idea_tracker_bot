import os

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey

from config import config


def get_engine():
    try:
        SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{config["DB_USER"]}:{config["DB_PASSWORD"]}@127.0.0.1:5432/{config["DB_NAME"]}'
    except BaseException:
        SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

    if SQLALCHEMY_DATABASE_URL.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
            'postgres://', "postgresql://", 1)
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    return engine


Base = declarative_base()


def get_db():
    engine = get_engine()
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True)


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    date_created = Column(DateTime)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref='items')
