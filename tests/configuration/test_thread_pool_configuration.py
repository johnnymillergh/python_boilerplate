from pytest_mock import MockerFixture

from python_boilerplate.configuration.thread_pool_configuration import (
    cleanup,
    configure,
    done_callback,
    executor,
)


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        assert False, f"{configure} raised an exception {ex}"


def test_executor_when_future_raising_exception():
    try:
        executor.submit(lambda x, y: x / y, 1, 0).add_done_callback(done_callback)
    except Exception as ex:
        assert False, f"{executor} raised an exception. {ex}"


def test_cleanup(mocker: MockerFixture):
    patched_executor = mocker.patch.object(executor, "shutdown")
    cleanup()
    patched_executor.assert_called_once()
