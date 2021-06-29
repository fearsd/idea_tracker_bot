"""Tests."""

from handlers import register_user


def test_sum():
    """Example test (sum)."""
    assert 2 + 2 == 4  # noqa: S101


def test_dividing():
    """Example test (dividing)."""
    assert 2 / 2 == 1  # noqa: S101


def test_register_user(test_db, telegram_id):
    """
    Test user registration.

    Parameters:
        test_db: Db session.
        telegram_id: User Telegram ID.
    """
    user_data = {'telegram_id': telegram_id}
    user = register_user(user_data=user_data, db=test_db)
    assert user.telegram_id == user_data['telegram_id']  # noqa: S101


def test_register_user_if_user_restarted_bot(test_db, telegram_id):
    """
    Test user registration if user restarted the bot.

    Parameters:
        test_db: Db session.
        telegram_id: User Telegram ID.
    """
    user_data = {'telegram_id': telegram_id}
    user_first_start = register_user(user_data=user_data, db=test_db)

    user_second_start = register_user(user_data=user_data, db=test_db)
    assert user_first_start.telegram_id == user_data['telegram_id']  # noqa: S101, E501
    assert user_first_start.telegram_id == user_second_start.telegram_id  # noqa: S101, E501
    assert user_first_start.id == user_second_start.id  # noqa: S101
