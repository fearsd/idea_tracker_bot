"""Pytest fixtures."""
import random

import pytest
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

import models


@pytest.fixture
def test_db():
    """
    Fixture that connects to test db.

    Yields:
        db: Db session
    """
    engine = create_engine('sqlite:///:memory:', echo=True)
    session_local = sessionmaker(bind=engine)
    db = session_local()
    models.Base.metadata.create_all(engine)
    try:
        yield db
    finally:
        models.Base.metadata.drop_all(bind=engine)
        db.close()


@pytest.fixture
def telegram_id():
    """
    Fixture that returns random telegram id.

    Returns:
        telegram_id: User Telegram ID.
    """
    start = 0
    end = 1000000
    return random.randint(start, end)  # noqa: S311 
