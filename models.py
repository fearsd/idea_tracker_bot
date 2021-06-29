"""Module has classes and methods to operate with db."""
import os

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey

from config import config


def get_engine():
    """
    Db engine.

    Returns:
        engine: Engine of db.
    """
    try:
        dialect = 'postgresql+psycopg2'
        database_uri = '{0}://{1}:{2}@127.0.0.1:5432/{3}'.format(
            dialect,
            config['DB_USER'],
            config['DB_PASSWORD'],
            config['DB_NAME'],
        )
    except KeyError:
        database_uri = os.environ['DATABASE_URL']

    if database_uri.startswith('postgres://'):
        database_uri = database_uri.replace('postgres://', 'postgresql://', 1)
    return create_engine(database_uri)


Base = declarative_base()


def get_db():
    """
    Db session.

    Yields:
        db: Db session
    """
    engine = get_engine()
    session_local = sessionmaker(
        bind=engine, autocommit=False, autoflush=False,
    )
    db = session_local()
    try:  # noqa: WPS501
        yield db
    finally:
        db.close()


class User(Base):
    """User model."""

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True)


class Item(Base):  # noqa: WPS110
    """Item model."""

    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    date_created = Column(DateTime)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='items')
