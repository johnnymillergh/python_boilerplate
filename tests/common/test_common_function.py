from loguru import logger

from python_boilerplate.common.common_function import get_login_user


def test_get_login_user():
    login_user = get_login_user()
    assert len(login_user) > 0
    logger.info(f"Current login user is [{login_user}]")
