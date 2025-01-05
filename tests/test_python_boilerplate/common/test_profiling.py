import asyncio
from time import sleep

import pytest

from python_boilerplate.common.profiling import (
    async_elapsed_time,
    cpu_profile,
    elapsed_time,
    mem_profile,
)


@mem_profile()
@elapsed_time(level="WARNING")
def time_consuming_function() -> str:
    sleep(3)
    return "done execution"


@cpu_profile()
@mem_profile()
@elapsed_time(level="INFO")
def time_consuming_function_raising_error() -> None:
    sleep(1)
    raise RuntimeError("Unknown exception")


@async_elapsed_time(level="WARNING")
async def async_time_consuming_function(input_string: str) -> str:
    await asyncio.sleep(1)
    if "exception" in input_string:
        raise RuntimeError(f"Unknown exception with: {input_string}")
    return f"Done with {input_string}"


def test_elapsed_time() -> None:
    try:
        result: str = time_consuming_function()
    except Exception as ex:
        pytest.fail(f"`time_consuming_function()` raised an exception {ex}")
    assert result is not None
    assert result == "done execution"


def test_time_consuming_function_raising_error() -> None:
    with pytest.raises(RuntimeError) as exc_info:
        time_consuming_function_raising_error()
    assert exc_info is not None
    assert exc_info.value is not None


@pytest.mark.asyncio
async def test_async_time_consuming_function_when_input_doesnt_contain_exception() -> None:
    result: str = await async_time_consuming_function("Hello, World!")
    assert result is not None
    assert result == "Done with Hello, World!"


@pytest.mark.asyncio
async def test_async_time_consuming_function_when_input_contains_exception() -> None:
    with pytest.raises(RuntimeError) as exc_info:
        await async_time_consuming_function("exception")
    assert exc_info is not None
    assert exc_info.value is not None
