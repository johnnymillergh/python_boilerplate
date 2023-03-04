import configparser
from typing import Final

from loguru import logger
from pyhocon import ConfigFactory, ConfigTree

from python_boilerplate.common.common_function import (
    PROJECT_ROOT_PATH,
    get_resources_dir,
)

# `application_conf` contains the configuration for the application.
application_conf: ConfigTree = ConfigFactory.parse_file(
    get_resources_dir() / "application.conf"
)

# setup.cfg contains the project constants
setup_cfg: Final = configparser.ConfigParser()
setup_cfg.read(PROJECT_ROOT_PATH / "setup.cfg")


def configure() -> None:
    """
    Configure application.
    """
    logger.warning(
        f"Application configuration loaded, {application_conf}, {setup_cfg.sections()}"
    )
