import pytest
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import models

@pytest.fixture
def test_db():
    engine = create_engine('sqlite:///:memory:', echo=True)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    models.Base.metadata.create_all(engine)
    try:
        yield db
    finally:
        models.Base.metadata.drop_all(bind=engine)
        db.close()