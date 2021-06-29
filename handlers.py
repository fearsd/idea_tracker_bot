"""This module contains business logic for message handlers."""
from models import User


def register_user(*, user_data, db):
    """
    Register new user.

    :param user_data: Data needed to create user.
    :type user_data: dict.
    :param db: Db session.
    :type db: sessionmaker.
    :returns: User -- The User model instance.
    """
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
