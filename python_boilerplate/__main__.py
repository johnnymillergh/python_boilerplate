import atexit
import os
import platform
import sys
import time
from pathlib import Path

from loguru import logger

from python_boilerplate.common.common_function import get_module_name
from python_boilerplate.configuration.application_configuration import (
    configure as application_configure,
)
from python_boilerplate.configuration.application_configuration import setup_cfg
from python_boilerplate.configuration.loguru_configuration import (
    configure as loguru_configure,
)
from python_boilerplate.configuration.thread_pool_configuration import (
    cleanup as thread_pool_cleanup,
)
from python_boilerplate.configuration.thread_pool_configuration import (
    configure as thread_pool_configure,
)
from python_boilerplate.message.email import __init__
from python_boilerplate.message.email import cleanup as email_cleanup
from python_boilerplate.repository.model.startup_log import StartupLog
from python_boilerplate.repository.startup_log_repository import (
    retain_startup_log,
    save,
    update_latest,
)
from python_boilerplate.repository.trace_log_repository import retain_trace_log

__start_time = time.perf_counter()


def startup():
    logger.info(
        f"Starting {get_module_name()} using Python {platform.python_version()} on "
        f"{platform.node()} with PID {os.getpid()} ({Path(__file__).parent})"
    )

    # Configuration
    application_configure()
    loguru_configure()
    thread_pool_configure()

    # Initialization
    __init__()

    # Saving startup log
    # Cannot save startup log in parallel, because the ThreadPoolExecutor won't be able to start another future
    # once the MainThread will end very soon.
    # executor.submit(save, StartupLog(command_line=" ".join(sys.argv))).add_done_callback(done_callback)
    save(StartupLog(command_line=" ".join(sys.argv)))

    elapsed = time.perf_counter() - __start_time
    logger.info(
        f"Started {get_module_name()}@{setup_cfg['metadata']['version']} in {round(elapsed, 3)} seconds "
        f"({round(elapsed * 1000, 2)} ms)"
    )


@atexit.register
def finalize() -> None:
    """
    Register `finalize()` function to be executed upon normal program termination.
    """
    logger.warning(f"Stopping {get_module_name()}, releasing system resources")
    # Retain logs, in case the size of the SQLite database will be increasing like crazy.
    retain_startup_log()
    retain_trace_log()
    # Shutdown tread pool and other connections
    thread_pool_cleanup()
    email_cleanup()
    update_latest()
    __end_elapsed = time.perf_counter() - __start_time
    logger.info(
        f"Stopped {get_module_name()}, running for {round(__end_elapsed, 3)} seconds "
        f"({round(__end_elapsed * 1000, 2)} ms) in total"
    )


def __main__() -> None:
    """
    Main function.
    """
    logger.info(f"Current module: {get_module_name()}")


if __name__ == "__main__":
    __main__()
