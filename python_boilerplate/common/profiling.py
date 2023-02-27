import functools
import time
from datetime import timedelta
from typing import Callable

from loguru import logger


def elapsed_time(level="INFO"):
    """
    The decorator to monitor the elapsed time of a function.

    Usage:
     * decorate the function with `@elapsed_time()` to profile the function with INFO log
     * decorate the function with `@elapsed_time("DEBUG")` to profile the function with DEBUG log

    https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar

    :param level: logging level, default is `INFO`. Available values: "TRACE", "DEBUG", "INFO", "WARNING", "ERROR"
    """

    def elapsed_time_wrapper(func: Callable):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
            start_time = time.perf_counter()
            return_value = func(*arg, **kwarg)
            elapsed = time.perf_counter() - start_time
            logger.log(
                level,
                f"{func.__qualname__}() -> elapsed time: {timedelta(seconds=elapsed)}",
            )
            return return_value

        return wrapped

    return elapsed_time_wrapper
