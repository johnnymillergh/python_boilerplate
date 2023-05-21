import logging
import platform
import sys
from logging import LogRecord

import arrow
from arrow import Arrow
from loguru import logger

from python_boilerplate.common.common_function import get_data_dir, get_module_name
from python_boilerplate.configuration.application_configuration import application_conf

_message_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level.icon} {level: <8}</level> | "
    "<magenta>{process.id}</magenta> | "
    "<blue>{thread.name: <15}</blue> | "
    "<cyan>{name}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)
# Remove a previously added handler and stop sending logs to its sink.
logger.remove(handler_id=None)
# Set up logging for log file
_logs_directory_path = get_data_dir("logs")
_log_file = (
    str(_logs_directory_path)
    + f"/{get_module_name()}.{platform.node()}."
    + "{time}.log"
)
log_level = application_conf.get_string("log_level")
logger.add(
    _log_file,
    level=log_level,
    format=_message_format,
    enqueue=True,
    # turn to false if in production to prevent data leaking
    backtrace=True,
    diagnose=True,
    rotation="00:00",
    retention="7 days",
    compression="gz",
    serialize=False,
)
# Override the default stderr (console)
logger.add(sys.stderr, level=log_level, format=_message_format)


class InterceptHandler(logging.Handler):
    """
    Intercept standard logging

    https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    https://gist.github.com/devsetgo/28c2edaca2d09e267dec46bb2e54b9e2
    """

    def emit(self, record: LogRecord) -> None:
        # Get corresponding Loguru level if it exists
        level: int | str
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            if frame.f_back is not None:
                frame = frame.f_back
                depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, f"{record.name} -> {record.getMessage()}"
        )


logging.basicConfig(handlers=[InterceptHandler()], level=0)
logger.info(f"{type(logger)} is intercepting standard logging")

for key, value in application_conf.get_config("log").items():
    logging.getLogger(key).setLevel(value)
    logger.info(f"Configured logger[{key}]'s level to {value}")


def retain_log_files() -> None:
    now = arrow.get()
    dates = {
        date.format("YYYY-MM-DD")
        for date in Arrow.range("day", now.shift(days=-7), end=now)
    }
    for file_path in _logs_directory_path.glob("*.log"):
        split_log_file_name = file_path.name.split(".")
        split_log_file_name.reverse()
        date_in_file_name = split_log_file_name[1][0:10]
        if date_in_file_name not in dates:
            logger.debug(f"Deleting log: {file_path}")
            file_path.unlink(missing_ok=True)


def configure() -> None:
    """
    Configure logging.
    """
    retain_log_files()
    logger.warning(f"Loguru logging configured, log_level: {log_level}")
