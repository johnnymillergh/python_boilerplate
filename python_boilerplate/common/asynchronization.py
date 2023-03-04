import functools
from typing import Callable

from loguru import logger

from python_boilerplate.configuration.thread_pool_configuration import (
    done_callback,
    executor,
)


def async_function(func: Callable):
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
    def wrapped(*arg, **kwarg):
        if arg and not kwarg:
            submitted_future = executor.submit(func, *arg)
        elif not arg and kwarg:
            submitted_future = executor.submit(func, **kwarg)
        elif arg and kwarg:
            submitted_future = executor.submit(func, *arg, **kwarg)
        else:
            submitted_future = executor.submit(func)
        submitted_future.add_done_callback(done_callback)
        logger.debug(
            f"Submitted future task {submitted_future} to run [{func.__qualname__}()] asynchronously"
        )
        return submitted_future

    return wrapped
