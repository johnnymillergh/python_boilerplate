import functools
import time
from typing import Any, Callable

from loguru import logger


def debounce(wait: float) -> Callable[..., Callable[..., None]]:
    """
    Debounce function decorator.
    @param wait: wait time in seconds
    @return: a decorated function
    """

    def decorator(func: Callable[..., None]) -> Callable[..., None]:
        last_called: float = 0

        @functools.wraps(func)
        def debounced_func(*args: Any, **kwargs: Any) -> None:
            nonlocal last_called
            elapsed = time.monotonic() - last_called
            if elapsed > wait:
                func(*args, **kwargs)
                last_called = time.monotonic()

        return debounced_func

    return decorator


def throttle(limit: float) -> Callable[..., Callable[..., None]]:
    """
    Throttle function decorator.
    @param limit: throttle limit in seconds
    @return: a decorated function
    """

    def decorator(func: Callable[..., None]) -> Callable[..., None]:
        last_called: float = 0
        called = False

        @functools.wraps(func)
        def throttled_func(*args: Any, **kwargs: Any) -> None:
            nonlocal last_called, called
            elapsed = time.monotonic() - last_called
            if not called:
                logger.debug("Calling func due to not called")
                called = True
                func(*args, **kwargs)
                last_called = time.monotonic()
            elif elapsed > limit:
                logger.debug("Calling func due to elapsed > limit")
                func(*args, **kwargs)
                last_called = time.monotonic()

        return throttled_func

    return decorator
