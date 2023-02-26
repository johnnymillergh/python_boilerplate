import asyncio
from time import sleep

import pytest
from loguru import logger
from pytest_mock import MockFixture

from python_boilerplate.common.debounce_throttle import (
    async_debounce,
    debounce,
    throttle,
)
from python_boilerplate.common.trace import async_trace, trace


def test_debounce() -> None:
    call_count: int = 3
    while call_count > 0:
        debounce_function()
        call_count -= 1
    sleep(2)


@pytest.mark.asyncio
async def test_async_debounce():
    try:
        asyncio.new_event_loop().run_until_complete(
            async_debounce_function() for _ in range(3)
        )
    except Exception as e:
        assert False, f"Failed to test throttle_function(). {e}"


def test_throttle(mocker: MockFixture) -> None:
    import tests

    spy = mocker.spy(tests.common.test_debounce_throttle, "throttle_function")
    call_count: int = 5
    try:
        while call_count > 0:
            throttle_function()
            call_count -= 1
            sleep(0.1)
    except Exception as ex:
        assert False, f"Failed to test throttle_function(). {ex}"
    spy.assert_called()


@trace
@debounce(1)
def debounce_function() -> None:
    logger.warning("'debounce_function' was called")


@async_debounce(0.25)
def async_debounce_function():
    logger.warning("'async_debounce_function' was called")


@async_trace
@throttle(0.25)
def throttle_function() -> None:
    logger.warning("'throttle_function' was called")
