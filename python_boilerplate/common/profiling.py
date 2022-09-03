import functools
import time
from typing import Callable

from loguru import logger


def elapsed_time(level="INFO"):
    """
    The decorator to monitor the elapsed time of a function.
    :param level: logging level, default is `INFO`
    """

    def elapsed_time_decorator(func: Callable):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
            start_time = time.time()
            return_value = func(*arg, **kwarg)
            end_time = time.time()
            logger.log(
                level,
                f"Elapsed {round(end_time - start_time, 4)}s for function {func.__qualname__}()",
            )
            return return_value

        return wrapped

    return elapsed_time_decorator
