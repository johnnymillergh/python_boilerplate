import pytest

from python_boilerplate.message.email import cleanup, init_smtp


def test_init() -> None:
    try:
        init_smtp()
    except Exception as ex:
        pytest.fail(f"{init_smtp} raised an exception {ex}")


def test_cleanup() -> None:
    try:
        cleanup()
    except Exception as ex:
        pytest.fail(f"{cleanup} raised an exception {ex}")
