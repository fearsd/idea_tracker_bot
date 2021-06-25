"""This module contains business logic for message handlers."""
from models import User


def register_user(*, data, db):
    # db = get_db()
    new_user = User(**data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
