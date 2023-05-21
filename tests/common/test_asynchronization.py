from concurrent.futures import Future
from time import sleep

from loguru import logger

from python_boilerplate.common.asynchronization import async_function


@async_function
def an_async_function(param1: str, param2: str) -> str:
    sleep(1)
    logger.info(f"Function's param1={param1}, param2={param2}")
    return f"Hello, got param1={param1}, param2={param2}"


@async_function
def another_async_function_without_args() -> None:
    sleep(1)
    logger.info(f"Hello from {another_async_function_without_args.__qualname__}")


def test_async_function_expected_no_errors() -> None:
    a_future: Future[str] = an_async_function("argument #1", "argument #2")
    assert a_future is not None
    assert type(a_future) is Future
    result = a_future.result()
    assert a_future.done() is True
    assert len(result) > 0
    assert result == "Hello, got param1=argument #1, param2=argument #2"
    logger.info(f"Got future result: {result}")


def test_async_function_pass_kwarg_expected_no_errors() -> None:
    a_future: Future[str] = an_async_function(
        param1="argument #1", param2="argument #2"
    )
    assert a_future is not None
    assert type(a_future) is Future
    result = a_future.result()
    assert a_future.done() is True
    assert len(result) > 0
    assert result == "Hello, got param1=argument #1, param2=argument #2"
    logger.info(f"Got future result: {result}")


def test_async_function_pass_arg_kwarg_expected_no_errors() -> None:
    a_future: Future[str] = an_async_function("argument #1", param2="argument #2")
    assert a_future is not None
    assert type(a_future) is Future
    result = a_future.result()
    assert a_future.done() is True
    assert len(result) > 0
    assert result == "Hello, got param1=argument #1, param2=argument #2"
    logger.info(f"Got future result: {result}")


def test_another_async_function_without_args_expected_no_errors() -> None:
    a_future: Future[None] = another_async_function_without_args()
    assert a_future is not None
    assert type(a_future) is Future
    result = a_future.result()
    assert a_future.done() is True
    assert result is None
