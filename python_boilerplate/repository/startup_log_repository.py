from datetime import datetime

import arrow
from loguru import logger

from python_boilerplate.common.common_function import get_module_name
from python_boilerplate.common.trace import trace
from python_boilerplate.repository.model.startup_log import StartupLog


@trace
def save(startup_log: StartupLog) -> StartupLog:
    """
    Save a new startup log.
    :param: a StartupLog needs to save
    :return: a StartupLog object
    """
    startup_log.save()
    return startup_log


def update_latest() -> None:
    latest = StartupLog.select().order_by(StartupLog.id.desc()).limit(1).execute()
    logger.debug(latest[0])
    now = datetime.now()
    StartupLog.update({StartupLog.exit_time: now, StartupLog.modified_time: now}).where(
        StartupLog.id == latest[0].id
    ).execute()


def retain_startup_log() -> int:
    a_week_ago = arrow.now("local").shift(days=-7).format("YYYY-MM-DD")
    affected_rows: int = (
        StartupLog.delete().where(StartupLog.startup_time < a_week_ago).execute()
    )
    # the affected_rows is always 1 no matter how many rows were deleted
    logger.debug(
        f"The app [{get_module_name()}] retains recent 7 days of startup log. "
        f"Deleted {affected_rows} records that are before {a_week_ago}"
    )
    return affected_rows
