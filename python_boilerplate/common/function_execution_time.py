import time
from typing import Callable

from loguru import logger


def elapsed_time(level="INFO"):
    """
    The decorator to monitor the elapsed time of a function.
    :param level: logging level, default is `INFO`
    """

    def elapsed_time_decorator(function: Callable):
        def wrapped(*arg, **kwarg):
            start_time = time.time()
            return_value = function(*arg, **kwarg)
            end_time = time.time()
            logger.log(
                level,
                f"Elapsed time of function {function}：{round(end_time - start_time, 4)}s",
            )
            return return_value

        return wrapped

    return elapsed_time_decorator
