from loguru import logger

from python_boilerplate.configuration.loguru_configuration import configure


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
        logger.exception(f"Oops! Exception occurred. {ex.__str__()}")
