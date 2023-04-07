import functools
import os
import time
from datetime import timedelta
from typing import Callable

import psutil
from loguru import logger


def elapsed_time(level="INFO"):
    """
    The decorator to monitor the elapsed time of a function.

    Usage:

    * decorate the function with `@elapsed_time()` to profile the function with INFO log
    >>> @elapsed_time()
    >>> def some_function():
    >>>    pass

    * decorate the function with `@elapsed_time("DEBUG")` to profile the function with DEBUG log
    >>> @elapsed_time("DEBUG")
    >>> def some_function():
    >>>    pass

    https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar

    :param level: logging level, default is "INFO". Available values: ["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"]
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


def get_memory_usage():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def get_cpu_usage():
    """
    Getting cpu_percent non-blocking (percentage since last call)
    """
    cpu_usage = psutil.cpu_percent()
    return cpu_usage


def mem_profile(level="INFO"):
    """
    The decorator to monitor the memory usage of a function.

    Usage:

    * decorate the function with `@mem_profile()` to profile the function with INFO log
    >>> @mem_profile()
    >>> def some_function():
    >>>    pass

    * decorate the function with `@mem_profile("DEBUG")` to profile the function with DEBUG log
    >>> @mem_profile("DEBUG")
    >>> def some_function():
    >>>    pass

    https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar

    :param level: logging level, default is "INFO". Available values: ["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"]
    """

    def mem_profile_wrapper(func: Callable):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
            mem_before = get_memory_usage()
            return_value = func(*arg, **kwarg)
            mem_after = get_memory_usage()
            logger.log(
                level,
                f"{func.__qualname__}() -> Mem before: {mem_before}, mem after: {mem_after}. "
                f"Consumed memory: {(mem_after - mem_before) / (1024 * 1024):.2f} MB",
            )
            return return_value

        return wrapped

    return mem_profile_wrapper


def cpu_profile(level="INFO"):
    """
    The decorator to monitor the CPU usage of a function.

    Usage:

    * decorate the function with `@mem_profile()` to profile the function with INFO log
    >>> @cpu_profile()
    >>> def some_function():
    >>>    pass

    * decorate the function with `@cpu_profile("DEBUG")` to profile the function with DEBUG log
    >>> @mem_profile("DEBUG")
    >>> def some_function():
    >>>    pass

    https://stackoverflow.com/questions/12295974/python-decorators-just-syntactic-sugar

    :param level: logging level, default is "INFO". Available values: ["TRACE", "DEBUG", "INFO", "WARNING", "ERROR"]
    """

    def cpu_profile_wrapper(func: Callable):
        @functools.wraps(func)
        def wrapped(*arg, **kwarg):
            cpu_before = get_cpu_usage()
            return_value = func(*arg, **kwarg)
            cpu_after = get_cpu_usage()
            logger.log(
                level,
                f"{func.__qualname__}() -> CPU before: {cpu_before}, CPU after: {cpu_after}, "
                f"delta: {(cpu_after - cpu_before):.2f}",
            )
            return return_value

        return wrapped

    return cpu_profile_wrapper
