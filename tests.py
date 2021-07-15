"""Tests."""
import datetime

from handlers import (add_new_idea, get_ideas_on_week,
                      register_user_or_find_existed)
from utils import ideas_to_text


def test_register_user(test_db, user_data):
    """
    Test user registration.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    user = register_user_or_find_existed(user_data=user_data, db=test_db)
    assert user.telegram_id == user_data['telegram_id']  # noqa: S101


def test_register_user_if_user_restarted_bot(test_db, user_data):
    """
    Test user registration if user restarted the bot.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    first_user = register_user_or_find_existed(
        user_data=user_data,
        db=test_db,
    )

    second_user = register_user_or_find_existed(
        user_data=user_data,
        db=test_db,
    )
    assert first_user.telegram_id == user_data['telegram_id']  # noqa: S101
    assert first_user.telegram_id == second_user.telegram_id  # noqa: S101
    assert first_user.id == second_user.id  # noqa: S101


def test_add_new_idea(test_db, user_data):
    """
    Test adding new idea.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    user = register_user_or_find_existed(user_data=user_data, db=test_db)
    idea_data = {
        'user_id': user.id,
        'body': 'text',
        'date_created': datetime.datetime.now(),
    }
    idea = add_new_idea(idea_data=idea_data, db=test_db)

    assert idea.user_id == idea_data['user_id']  # noqa: S101
    assert idea.body == idea_data['body']  # noqa: S101
    assert idea.date_created == idea_data['date_created']  # noqa: S101


def test_get_ideas(test_db, user_data):  # noqa: WPS210
    """
    Test getting ideas.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    user = register_user_or_find_existed(user_data=user_data, db=test_db)

    user_data = {'telegram_id': 1234}
    user2 = register_user_or_find_existed(user_data=user_data, db=test_db)

    idea_data = {
        'user_id': user.id,
        'body': 'text',
        'date_created': datetime.datetime.now(),
    }
    idea_data2 = {
        'user_id': user2.id,
        'body': 'text',
        'date_created': datetime.datetime.now(),
    }
    add_new_idea(idea_data=idea_data, db=test_db)
    add_new_idea(idea_data=idea_data, db=test_db)
    add_new_idea(idea_data=idea_data2, db=test_db)

    ideas = get_ideas_on_week(user=user, db=test_db)
    assert len(list(ideas)) == 2  # noqa: S101


def test_ideas_to_text(test_db, user_data):
    """
    Test ideas to text.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    user = register_user_or_find_existed(user_data=user_data, db=test_db)

    idea_data = {
        'user_id': user.id,
        'body': 'text',
        'date_created': datetime.datetime.now(),
    }
    add_new_idea(idea_data=idea_data, db=test_db)
    add_new_idea(idea_data=idea_data, db=test_db)
    ideas = list(get_ideas_on_week(user=user, db=test_db))

    mess = ideas_to_text(ideas)

    assert type(mess).__name__ == 'str'  # noqa: S101
