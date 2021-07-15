"""This module contains business logic for message handlers."""
from models import User, Item


def register_user_or_find_existed(*, user_data, db):
    """
    Registers new user or find it by telegram id if he exists.

    Parameters:
        user_data: Data needed to create user.
        db: Db session.

    Returns:
        new_user: The User model instance.
    """
    try:
        user = db.query(User).filter_by(
            telegram_id=user_data['telegram_id'],
        ).one()
    except BaseException:  # noqa: E722, B001, WPS424
        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    return user


def add_new_idea(*, idea_data, db):
    """
    Creates new idea.

    Parameters:
        idea_data: Data needed to create idea.
        db: Db session.
    
    Returns:
        new_idea: The Item model instance.
    """
    new_idea = Item(**idea_data)
    db.add(new_idea)
    db.commit()
    db.refresh(new_idea)
    return new_idea
