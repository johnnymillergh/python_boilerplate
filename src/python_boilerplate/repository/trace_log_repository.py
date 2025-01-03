import arrow
from loguru import logger

from python_boilerplate.common.common_function import get_module_name
from python_boilerplate.repository.model.trace_log import TraceLog


def save(trace_log: TraceLog) -> TraceLog:
    trace_log.save()
    return trace_log


def retain_trace_log() -> int:
    a_week_ago = arrow.now("local").shift(days=-7).format("YYYY-MM-DD")
    affected_rows: int = TraceLog.delete().where(TraceLog.start_time < a_week_ago).execute()
    # the affected_rows is always 1 no matter how many rows were deleted
    logger.debug(
        f"The app [{get_module_name()}] retains recent 7 days of trace log. "
        f"Deleted {affected_rows} records that are before {a_week_ago}"
    )
    return affected_rows
