import sys

import arrow
from loguru import logger

from python_boilerplate.common.trace import trace
from python_boilerplate.repository.model.startup_log import StartupLog


@trace
def save() -> StartupLog:
    """
    Save a new startup log.
    :return: a StartupLog object
    """
    startup_log: StartupLog = StartupLog(command_line=" ".join(sys.argv))
    startup_log.save()
    retain_startup_log()
    return startup_log


def retain_startup_log() -> int:
    a_week_ago = arrow.now().shift(days=-7).format("YYYY-MM-DD")
    affected_rows: int = (
        StartupLog.delete().where(StartupLog.startup_time < a_week_ago).execute()
    )
    # the affected_rows is always 1 no matter how many rows were deleted
    logger.debug(
        f"The program retains recent 7 days of startup log. "
        f"Deleted {affected_rows} records that are before {a_week_ago}"
    )
    return affected_rows
