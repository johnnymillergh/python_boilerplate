from time import sleep

from loguru import logger

from python_boilerplate.common.debounce_throttle import (
    async_debounce,
    debounce,
    throttle,
)
from python_boilerplate.common.trace import trace


def test_debounce() -> None:
    call_count: int = 3
    while call_count > 0:
        debounce_function()
        call_count -= 1
    sleep(2)


# @pytest.mark.asyncio
# async def test_async_debounce():
#     try:
#         await asyncio.new_event_loop().run_until_complete(async_debounce_function() for _ in range(3))
#     except Exception:
#         assert False, "Failed to test throttle_function()"


def test_throttle() -> None:
    call_count: int = 5
    try:
        while call_count > 0:
            throttle_function()
            call_count -= 1
            sleep(0.24)
    except Exception as ex:
        assert False, f"Failed to test throttle_function(). {ex}"


@trace
@debounce(1)
def debounce_function() -> None:
    logger.warning("'debounce_function' was called")


@async_debounce(0.25)
def async_debounce_function():
    logger.warning("'async_debounce_function' was called")


@throttle(0.25)
def throttle_function() -> None:
    logger.warning("'throttle_function' was called")
