import pytest
from loguru import logger
from tenacity import RetryError

from python_boilerplate.demo.tenacity_usage import (
    customized_retry_logic_function,
    different_exceptions_possible,
    exception_function_1,
    exception_function_2,
)


def test_exception_function_1() -> None:
    with pytest.raises(RetryError):
        exception_function_1()


def test_exception_function_2() -> None:
    with pytest.raises(RetryError):
        exception_function_2()


def test_different_exceptions_possible() -> None:
    with pytest.raises(RetryError):
        different_exceptions_possible(1)
    with pytest.raises(RetryError):
        different_exceptions_possible(2)
    with pytest.raises(TypeError):
        different_exceptions_possible(3)
    assert different_exceptions_possible(4) == "success"


def test_customized_retry_logic_function() -> None:
    try:
        customized_retry_logic_function(240)
    except RetryError as e:
        logger.warning(f"RetryError was raised. {e}")
