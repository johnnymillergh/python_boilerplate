import functools
import inspect
import json
from datetime import datetime
from typing import Any, Callable, TypeVar

from loguru import logger

from python_boilerplate.common.common_function import json_serial
from python_boilerplate.configuration.thread_pool_configuration import (
    done_callback,
    executor,
)
from python_boilerplate.repository.model.trace_log import TraceLog
from python_boilerplate.repository.trace_log_repository import save

R = TypeVar("R")


def async_trace(func: Callable[..., R]) -> Callable[..., R]:
    """
    The decorator to trace Python function asynchronously,
    which writes trace_log data in different threads (thread pool).

    Usage:
     * decorate a function with `@async_trace`

    :param func: a function to be traced
    """

    @functools.wraps(func)
    def wrapped(*arg: Any, **kwarg: Any) -> Any:
        function_arguments = {"arg": arg, "kwarg": kwarg}
        trace_log = TraceLog(
            called_by=inspect.stack()[1][3],
            function_qualified_name=func.__qualname__,
            function_arguments=json.dumps(function_arguments, default=json_serial),
        )
        executor.submit(
            save,
            trace_log,
        ).add_done_callback(done_callback)
        try:
            return func(*arg, **kwarg)
        except Exception as e:
            logger.warning(f"Captured exception while recording trace. {e}")
            # Don't swallow exceptions
            raise e
        finally:
            now = datetime.now()
            trace_log.end_time = now
            trace_log.modified_time = now
            executor.submit(
                save,
                trace_log,
            ).add_done_callback(done_callback)

    return wrapped


def trace(func: Callable[[Any], R]) -> Callable[[Any], R]:
    """
    The decorator to trace Python function synchronously,
    which will always record the end_time of the execution of a function in the same thread.

    Usage:
     * decorate a function with `@trace`

    :param func: a function to be traced
    """

    @functools.wraps(func)
    def wrapped(*arg: Any, **kwarg: Any) -> Any:
        function_arguments = {"arg": arg, "kwarg": kwarg}
        trace_log = TraceLog(
            called_by=inspect.stack()[1][3],
            function_qualified_name=func.__qualname__,
            function_arguments=json.dumps(function_arguments, default=json_serial),
        )
        trace_log.save()
        try:
            # Executing the function
            return func(*arg, **kwarg)
        except Exception as e:
            logger.warning(f"Captured exception while recording trace. {e}")
            # Don't swallow exceptions
            raise e
        finally:
            now = datetime.now()
            trace_log.end_time = now
            trace_log.modified_time = now
            trace_log.save()

    return wrapped
