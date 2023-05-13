import asyncio
from typing import Any, Coroutine

import pytest
from loguru import logger

from python_boilerplate.demo.async_demo import (
    coroutine1,
    coroutine2,
    coroutine3,
    non_coroutine,
)


@pytest.fixture(scope="session", autouse=True)
def setup() -> None:
    logger.info(f"Setting up tests for {__file__}")


@pytest.mark.asyncio
async def test_coroutine1() -> None:
    result: int = await coroutine1()
    assert type(result) == int
    assert result == 42
    logger.info(f"Result: {result}")


@pytest.mark.asyncio
async def test_coroutine2() -> None:
    result: str = await coroutine2()
    assert type(result) == str
    assert result == "Hello, world!"
    logger.info(f"Result: {result}")


@pytest.mark.asyncio
async def test_coroutine3() -> None:
    with pytest.raises(ValueError) as exc_info:
        await coroutine3()
    assert exc_info is not None
    assert exc_info.value is not None
    assert isinstance(exc_info.value, ValueError) is True
    logger.info(f"Async function `coroutine3()` raised exception: {exc_info.value}")


@pytest.mark.asyncio
async def test_non_coroutine() -> None:
    with pytest.raises(TypeError) as exc_info:
        await non_coroutine()
    assert exc_info is not None
    assert exc_info.value is not None
    assert type(exc_info.value) is TypeError
    logger.info(
        f"Non-async function `non_coroutine()` raised exception: {exc_info.value}"
    )


@pytest.mark.asyncio
async def test_running_coroutine1_and_coroutine2_sequentially() -> None:
    result1: int = await coroutine1()
    result2: str = await coroutine2()
    assert result1 is not None
    assert result1 == 42
    assert result2 is not None
    assert result2 == "Hello, world!"


@pytest.mark.asyncio
async def test_running_coroutine1_and_coroutine2_concurrently() -> None:
    coroutine_1: Coroutine[Any, Any, int] = coroutine1()
    coroutine_2: Coroutine[Any, Any, str] = coroutine2()
    gathered_results: list[Any] = await asyncio.gather(coroutine_1, coroutine_2)
    assert type(gathered_results) == list
    assert len(gathered_results) == 2
    assert type(gathered_results[0]) == int
    assert type(gathered_results[1]) == str
    logger.info(
        f"Type of `gathered_results`: {type(gathered_results)}, {gathered_results}"
    )


@pytest.mark.asyncio
async def test_running_coroutine1_2_3_concurrently() -> None:
    gathered_results: list[Any] = await asyncio.gather(
        *[coroutine1(), coroutine2(), coroutine3()], return_exceptions=True
    )
    logger.info(
        f"Type of `gathered_results`: {type(gathered_results)}, {gathered_results}"
    )
    assert type(gathered_results) == list
    assert len(gathered_results) == 3
    assert type(gathered_results[0]) == int
    assert type(gathered_results[1]) == str
    assert type(gathered_results[2]) is ValueError
