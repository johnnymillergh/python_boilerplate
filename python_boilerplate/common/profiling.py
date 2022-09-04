import functools
import time
from typing import Callable

from loguru import logger


def elapsed_time(level="INFO"):
    """
    The decorator to monitor the elapsed time of a function.

    Usage:
     * decorate the function with `@elapsed_time()` to profile the function with INFO log
     * decorate the function with `@elapsed_time("DEBUG")` to profile the function with DEBUG log

    https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar

    :param level: logging level, default is `INFO`
    """

    def elapsed_time_wrapper(func: Callable):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
            start_time = time.time()
            return_value = func(*arg, **kwarg)
            end_time = time.time()
            logger.log(
                level,
                f"The function [{func.__qualname__}()] elapsed {round(end_time - start_time, 4)}s "
                f"({round((end_time - start_time) * 1000, 4)}ms)",
            )
            return return_value

        return wrapped

    return elapsed_time_wrapper
