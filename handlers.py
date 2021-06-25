"""This module contains business logic for message handlers."""
from models import User


def register_user(*, user_data, db):
    """Register new user."""
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
