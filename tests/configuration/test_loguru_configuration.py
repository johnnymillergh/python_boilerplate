from pathlib import Path

from loguru import logger
from pytest_mock import MockerFixture

from python_boilerplate.configuration.loguru_configuration import (
    configure,
    retain_log_files,
)


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        assert False, f"{configure} raised an exception {ex}"


def test_log_exception() -> None:
    try:
        divided_by_zero = 5 / 0
        logger.info(f"divided_by_zero = {divided_by_zero}")
    except Exception as ex:
        logger.exception(f"Oops! Exception occurred. {ex}")


def test_retain_log_files(mocker: MockerFixture) -> None:
    path_list = [
        Path(
            "python_boilerplate.johnnys-macbook-pro-2017.local.2023-05-01_08-42-03_086829.log"
        )
    ]
    patch = mocker.patch(
        "pathlib.Path.glob", return_value=(element for element in path_list)
    )
    retain_log_files()
    patch.assert_called()
