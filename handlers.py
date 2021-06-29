"""This module contains business logic for message handlers."""
from models import User


def register_user(*, user_data, db):
    """
    Register new user.

    Parameters:
        user_data: Data needed to create user.
        db: Db session.

    Returns:
        new_user: The User model instance.
    """
    try:
        user = db.query(User).filter_by(telegram_id=user_data['telegram_id']).one()
    except:
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    else:
        return user
