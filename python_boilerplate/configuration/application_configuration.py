from loguru import logger
from pyhocon import ConfigFactory, ConfigTree

from python_boilerplate.function_collection import get_resources_dir

# `application_conf` contains the configuration for the application.
application_conf: ConfigTree = ConfigFactory.parse_file(
    get_resources_dir() / "application.conf"
)


def configure() -> None:
    """
    Configure application.
    """
    logger.warning(f"Application configuration loaded, {application_conf}")
