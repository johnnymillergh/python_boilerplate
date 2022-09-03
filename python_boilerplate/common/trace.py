import inspect
import json
from typing import Callable

from python_boilerplate.configuration.thread_pool_configuration import executor
from python_boilerplate.repository.model.trace_log import TraceLog


def trace(func: Callable):
    def wrapped(*arg, **kwarg):
        function_arguments = {"arg": arg, "kwarg": kwarg}
        trace_log = TraceLog(
            called_by=inspect.stack()[1][3],
            function_qualified_name=func.__qualname__,
            function_arguments=json.dumps(
                function_arguments, default=lambda x: x.__dict__
            ),
        )
        executor.submit(lambda x: x.save(), trace_log)
        return func(*arg, **kwarg)

    return wrapped
