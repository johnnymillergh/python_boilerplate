from loguru import logger
from pytest_mock import MockerFixture

from python_boilerplate.common.common_function import get_cpu_count, get_login_user


def test_get_cpu_count_when_cpu_count_is_none_then_returns_4(mocker: MockerFixture):
    with mocker.mock_module.patch(target="os.cpu_count") as patched:
        patched.return_value = None
        cpu_count = get_cpu_count()
        patched.assert_called_once()
        assert cpu_count == 4


def test_get_login_user():
    login_user = get_login_user()
    assert len(login_user) > 0
    logger.info(f"Current login user is [{login_user}]")


def test_get_login_user_when_exception_raised_then_returns_default_user(
    mocker: MockerFixture,
):
    with mocker.mock_module.patch(target="getpass.getuser") as patched:
        patched.side_effect = Exception("Mocked exception")
        user = get_login_user()
        patched.assert_called_once()
        assert user == "default_user"
