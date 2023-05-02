import functools
import os
import time
from datetime import timedelta
from typing import Any, Callable, TypeVar

import psutil
from loguru import logger

R = TypeVar("R")


def elapsed_time(level: str = "INFO") -> Callable[..., Callable[..., R]]:
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

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def wrapped(*arg: Any, **kwarg: Any) -> Any:
            start_time = time.perf_counter()
            return_value = func(*arg, **kwarg)
            elapsed = time.perf_counter() - start_time
            logger.log(
                level,
                f"{func.__qualname__}() -> elapsed time: {timedelta(seconds=elapsed)}",
            )
            return return_value

        return wrapped

    return decorator


def get_memory_usage() -> int:
    """
    Gets the usage of memory
    :return: memory usage in bytes
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def get_cpu_usage() -> float:
    """
    Getting cpu_percent non-blocking (percentage since last call)
    :return: CPU usage
    """
    cpu_usage = psutil.cpu_percent()
    return cpu_usage


def mem_profile(level: str = "INFO") -> Callable[..., Callable[..., R]]:
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

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def wrapped(*arg: Any, **kwarg: Any) -> Any:
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

    return decorator


def cpu_profile(level: str = "INFO") -> Callable[..., Callable[..., R]]:
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

    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @functools.wraps(func)
        def wrapped(*arg: Any, **kwarg: Any) -> Any:
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

    return decorator
