import pytest
from pytest_mock import MockerFixture

from python_boilerplate.common.asynchronization import done_callback
from python_boilerplate.configuration.thread_pool_configuration import (
    cleanup,
    configure,
    executor,
)


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        pytest.fail(f"{configure} raised an exception {ex}")


def test_executor_when_future_raising_exception() -> None:
    try:
        executor.submit(lambda x, y: x / y, 1, 0).add_done_callback(done_callback)
    except Exception as ex:
        pytest.fail(f"{executor} raised an exception. {ex}")


def test_cleanup(mocker: MockerFixture) -> None:
    # pytest-mock, patch an object, https://pytest-mock.readthedocs.io/en/latest/usage.html
    executor_patch = mocker.patch.object(executor, "shutdown")
    cleanup()
    executor_patch.assert_called_once()
