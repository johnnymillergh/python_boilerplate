from concurrent.futures import Future
from time import sleep

import arrow
from loguru import logger

from python_boilerplate.common.asynchronization import async_function


@async_function
def an_async_function(param1: str, param2: str):
    sleep(1)
    logger.info(f"Function's param1={param1}, param2={param2}")
    return f"Hello, got param1={param1}, param2={param2}"


@async_function
def another_async_function_without_args():
    sleep(1)
    logger.info(f"Hello from {another_async_function_without_args.__qualname__}")


def test_async_function_expected_no_errors():
    a_future: Future = an_async_function(  # type: ignore
        arrow.now().__str__(), arrow.now().shift(days=-1).__str__()
    )
    assert a_future is not None
    result = a_future.result()
    assert len(result) > 0
    logger.info(f"Got future result: {result}")


def test_async_function_pass_kwarg_expected_no_errors():
    a_future: Future = an_async_function(  # type: ignore
        param1=arrow.now().__str__(), param2=arrow.now().shift(days=-1).__str__()
    )
    assert a_future is not None
    result = a_future.result()
    assert len(result) > 0
    logger.info(f"Got future result: {result}")


def test_async_function_pass_arg_kwarg_expected_no_errors():
    a_future: Future = an_async_function(  # type: ignore
        arrow.now().__str__(), param2=arrow.now().shift(days=-1).__str__()
    )
    assert a_future is not None
    result = a_future.result()
    assert len(result) > 0
    logger.info(f"Got future result: {result}")


def test_another_async_function_without_args_expected_no_errors():
    try:
        another_async_function_without_args()
    except Exception as ex:
        assert False, f"{another_async_function_without_args} raised an exception {ex}"
