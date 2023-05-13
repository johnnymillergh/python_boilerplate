import functools
import time
from typing import Any, Callable, Optional, TypeVar

from loguru import logger

R = TypeVar("R")


def debounce(wait: float) -> Callable[..., Callable[..., Optional[R]]]:
    """
    Debounce function decorator.

    :param wait: wait time in seconds
    :return: a decorated function
    """

    def decorator(func: Callable[..., Optional[R]]) -> Callable[..., Optional[R]]:
        last_called: float = 0

        @functools.wraps(func)
        def debounced_func(*args: Any, **kwargs: Any) -> Optional[R]:
            nonlocal last_called
            elapsed = time.monotonic() - last_called
            if elapsed > wait:
                logger.debug("Calling function due to elapsed > wait time")
                result: Optional[R] = func(*args, **kwargs)
                last_called = time.monotonic()
                return result
            else:
                logger.debug(
                    f"Refused to call function {func.__qualname__}(args={args}, kwargs={kwargs})"
                )
                return None

        return debounced_func

    return decorator


def throttle(limit: float) -> Callable[..., Callable[..., Optional[R]]]:
    """
    Throttle function decorator.

    :param limit: throttle limit in seconds
    :return: a decorated function
    """

    def decorator(func: Callable[..., Optional[R]]) -> Callable[..., Optional[R]]:
        last_called: float = 0
        called = False

        @functools.wraps(func)
        def throttled_func(*args: Any, **kwargs: Any) -> Optional[R]:
            nonlocal last_called, called
            elapsed = time.monotonic() - last_called
            if not called:
                logger.debug("Calling func due to not called")
                called = True
                result = func(*args, **kwargs)
                last_called = time.monotonic()
                return result
            elif elapsed > limit:
                logger.debug("Calling func due to elapsed > limit")
                result = func(*args, **kwargs)
                last_called = time.monotonic()
                return result
            else:
                logger.debug(
                    f"Refused to call function `{func.__qualname__}`(args={args}, kwargs={kwargs})"
                )
                return None

        return throttled_func

    return decorator
