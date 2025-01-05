from __future__ import annotations

import getpass
import os
from datetime import date, datetime
from math import ceil
from pathlib import Path
from typing import Any, Final

from loguru import logger

# pathlib — Object-oriented filesystem paths
# https://docs.python.org/3/library/pathlib.html

# Path Correspondence to tools in the os module
# https://docs.python.org/3/library/pathlib.html#correspondence-to-tools-in-the-os-module

PROJECT_ROOT_PATH: Final = Path(__file__).parent.parent.parent.parent
MODULE_ROOT_PATH: Final = Path(__file__).parent.parent


def get_data_dir(sub_path: str = "") -> Path:
    """
    Get the data directory of the project.

    :param sub_path: the sub path (directory) under the `data` directory, Must NOT start with `/`.
    If not exists, the sub path will be created.
    """
    data_dir = PROJECT_ROOT_PATH / "data"
    if len(sub_path) > 0:
        data_dir = data_dir / sub_path
    if not data_dir.exists():
        # If parents are false (the default), a missing parent raises FileNotFoundError.
        # If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.
        data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_resources_dir() -> Path:
    """Get the resources directory of the project."""
    return MODULE_ROOT_PATH / "resources"


def get_module_name() -> str:
    """Get the name of the current module."""
    return MODULE_ROOT_PATH.name


def get_cpu_count() -> int:
    """Get CPU count, default is 4."""
    cpu_count = os.cpu_count()
    if cpu_count is not None:
        return cpu_count
    return 4


def get_login_user() -> str:
    """
    Get current login user who is using the OS.

    :return: the username
    """
    try:
        return getpass.getuser()
    except Exception as ex:
        logger.error(f"Failed to get current login user, falling back to `default_user`. {ex}")
        return "default_user"


def json_serial(obj: Any) -> str | dict[str, Any]:
    """
    JSON serializer for objects not serializable by default json code.

    https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable/36142844#36142844

    :param obj: on object needs to be serialized
    :return: string or dictionary
    """
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, set):
        return str(obj)
    return obj.__dict__


def chunk_into_n(a_list: list[Any], n: int) -> list[list[Any]]:
    """
    Chunk a list into smaller chunks.

    :param a_list: a list
    :param n: the number of chunks going to be split
    :return: chunks list
    """
    size = ceil(len(a_list) / n)
    return [a_list[x * size : x * size + size] for x in list(range(n))]
