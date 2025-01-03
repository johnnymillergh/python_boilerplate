from typing import Final

import tomllib
from loguru import logger
from pyhocon import ConfigFactory

from python_boilerplate.common.common_function import (
    PROJECT_ROOT_PATH,
    get_resources_dir,
)

# `application_conf` contains the configuration for the application.
application_conf: Final = ConfigFactory.parse_file(get_resources_dir() / "application.conf")

_pyproject_toml_file: Final = PROJECT_ROOT_PATH / "pyproject.toml"
if not _pyproject_toml_file.exists() or not _pyproject_toml_file.is_file():
    error = f"File not found: {_pyproject_toml_file}"
    logger.error(error)
    raise FileNotFoundError(error)
with _pyproject_toml_file.open("rb") as file:
    pyproject_toml: Final = tomllib.load(file)


def configure() -> None:
    """Configure application."""
    logger.warning(f"Application configuration loaded, {application_conf}, {pyproject_toml['tool']['poetry']['name']}")


if __name__ == "__main__":
    configure()
