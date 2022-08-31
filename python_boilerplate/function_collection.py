import os

_PROJECT_ROOT = os.path.abspath(f"{__file__}{os.path.sep}..{os.path.sep}..")
_CURRENT_FILE_PATH = os.path.abspath(__file__)


def get_root_path() -> str:
    """
    Get the root path of the project.
    """
    return os.path.dirname(_CURRENT_FILE_PATH)


def get_data_dir(sub_path="") -> str:
    """
    Get the data directory of the project.

    :param sub_path: the sub path under the `data` directory. If not exists, the sub path will be created.
    """
    if len(sub_path) > 0:
        data_dir = f"{_PROJECT_ROOT.__str__()}{os.path.sep}data{os.path.sep}{sub_path}"
    else:
        data_dir = f"{_PROJECT_ROOT.__str__()}{os.path.sep}data"
    os.makedirs(data_dir, exist_ok=True)
    return data_dir


def get_resources_dir() -> str:
    """
    Get the resources directory of the project.
    """
    return f"{get_root_path()}{os.path.sep}resources"


def get_module_name() -> str:
    """
    Get the name of the current module.
    """
    path_list = _CURRENT_FILE_PATH.split(os.path.sep)
    return path_list[len(path_list) - 2]


def get_cpu_count() -> int:
    """
    Get CPU count, default is 4
    """
    cpu_count = os.cpu_count()
    if cpu_count is not None:
        return cpu_count
    else:
        return 4
