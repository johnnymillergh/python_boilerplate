import atexit

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
from python_boilerplate.repository.startup_log_repository import save

# Configuration
application_configure()
loguru_configure()
thread_pool_configure()

# Initialization
__init__()
logger.info(f"Application [{get_module_name()}] started")
save()


@atexit.register
def finalize() -> None:
    """
    Register `finalize()` function to be executed upon normal program termination.
    """
    logger.warning("Cleaning up…")
    thread_pool_cleanup()
    email_cleanup()
