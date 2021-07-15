"""Tests."""
import datetime
from handlers import add_new_idea, register_user_or_find_existed


def test_sum():
    """Example test (sum)."""
    assert 2 + 2 == 4  # noqa: S101


def test_dividing():
    """Example test (dividing)."""
    assert 2 / 2 == 1  # noqa: S101


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
    user_first_start = register_user_or_find_existed(user_data=user_data, db=test_db)

    user_second_start = register_user_or_find_existed(user_data=user_data, db=test_db)
    assert user_first_start.telegram_id == user_data['telegram_id']  # noqa: S101, E501
    assert user_first_start.telegram_id == user_second_start.telegram_id  # noqa: S101, E501
    assert user_first_start.id == user_second_start.id  # noqa: S101


def test_add_new_idea(test_db, user_data):
    """
    Tests adding new idea.

    Parameters:
        test_db: Db session.
        user_data: User data.
    """
    user = register_user_or_find_existed(user_data=user_data, db=test_db)
    idea_data = {
        'user_id': user.id,
        'body': 'text',
        'date_created': datetime.datetime.now()
    }
    idea = add_new_idea(idea_data=idea_data, db=test_db)

    assert idea.user_id == idea_data['user_id']  # noqa: S101
    assert idea.body == idea_data['body']  # noqa: S101
    assert idea.date_created == idea_data['date_created']  # noqa: S101
