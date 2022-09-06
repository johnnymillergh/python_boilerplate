import functools
import inspect
import json
from typing import Callable

from python_boilerplate.common.common_function import json_serial
from python_boilerplate.configuration.thread_pool_configuration import (
    done_callback,
    executor,
)
from python_boilerplate.repository.model.trace_log import TraceLog
from python_boilerplate.repository.trace_log_repository import save


def trace(func: Callable):
    """
    The decorator to trace Python function asynchronously.

    Usage:
     * decorate a function with `@trace`

    :param func: a function to be traced
    """

    @functools.wraps(func)
    def wrapped(*arg, **kwarg):
        function_arguments = {"arg": arg, "kwarg": kwarg}
        executor.submit(
            save,
            TraceLog(
                called_by=inspect.stack()[1][3],
                function_qualified_name=func.__qualname__,
                function_arguments=json.dumps(function_arguments, default=json_serial),
            ),
        ).add_done_callback(done_callback)
        return func(*arg, **kwarg)

    return wrapped
