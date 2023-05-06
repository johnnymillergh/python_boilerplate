import functools
import inspect
from concurrent.futures import Future
from typing import Any, Callable, TypeVar

from loguru import logger

from python_boilerplate.configuration.thread_pool_configuration import (
    done_callback,
    executor,
)

R = TypeVar("R")


def async_function(func: Callable[..., R]) -> Callable[..., Future[R]]:
    """
    An easy way to implement multi-tread feature with thread pool. The decorator to run function in thread pool.
    The return value of decorated function will be `concurrent.futures._base.Future`.

    Usage: decorate the function with `@async_function`. For example,

    * a function that accepts one integer argument:
    >>> @async_function
    >>> def an_async_function(a_int: int):
    >>>     pass

    * a function without argument:
    >>> @async_function
    >>> def an_async_function():
    >>>   pass

    https://stackoverflow.com/questions/37203950/decorator-for-extra-thread

    :param func: function to run in thread pool
    """

    @functools.wraps(func)
    def wrapped(*arg: Any, **kwarg: Any) -> Future[R]:
        module = inspect.getmodule(func)
        if arg and not kwarg:
            submitted_future = executor.submit(func, *arg)
            logger.debug(
                f"Submitted future task to run function asynchronously: "
                f"{module}.{func.__qualname__}(*arg)"
            )
        elif not arg and kwarg:
            submitted_future = executor.submit(func, **kwarg)
            logger.debug(
                f"Submitted future task to run function asynchronously: "
                f"{module}.{func.__qualname__}(**kwarg)"
            )
        elif arg and kwarg:
            submitted_future = executor.submit(func, *arg, **kwarg)
            logger.debug(
                f"Submitted future task to run function asynchronously: "
                f"{module}.{func.__qualname__}(*arg, **kwarg)"
            )
        else:
            submitted_future = executor.submit(func)
            logger.debug(
                f"Submitted future task to run function asynchronously: "
                f"{module}.{func.__qualname__}()"
            )
        submitted_future.add_done_callback(done_callback)
        return submitted_future

    return wrapped
