import pytest

from handlers import register_user


def test_sum():
    assert 2 + 2 == 4


def test_dividing():
    assert 2 / 2 == 1


def test_register_user(test_db):
    data = {'telegram_id': 1232313}
    user = register_user(data=data, db=test_db)
    assert user.telegram_id == data['telegram_id']
    assert 'id' in dir(user)
