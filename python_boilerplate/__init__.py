import atexit
import sys

from loguru import logger

from python_boilerplate.common.common_function import get_module_name
from python_boilerplate.configuration.application_configuration import (
    configure as application_configure,
)
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
)
from python_boilerplate.repository.trace_log_repository import retain_trace_log

# Configuration
application_configure()
loguru_configure()
thread_pool_configure()

# Initialization
__init__()
logger.info(f"Application [{get_module_name()}] started")

# Saving startup log
# Cannot save startup log in parallel, because the ThreadPoolExecutor won't be able to start another future
# once the MainThread will end very soon.
# executor.submit(save, StartupLog(command_line=" ".join(sys.argv))).add_done_callback(done_callback)
save(StartupLog(command_line=" ".join(sys.argv)))


@atexit.register
def finalize() -> None:
    """
    Register `finalize()` function to be executed upon normal program termination.
    """
    logger.warning("Cleaning up…")
    # Retain logs, in case the size of the SQLite database will be increasing like crazy.
    retain_startup_log()
    retain_trace_log()
    # Shutdown tread pool and other connections
    thread_pool_cleanup()
    email_cleanup()
