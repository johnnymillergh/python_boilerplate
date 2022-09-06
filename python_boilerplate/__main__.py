from loguru import logger

from python_boilerplate.common.common_function import get_module_name


def __main__() -> None:
    """
    Main function.
    """
    logger.info(f"Current module: {get_module_name()}")


if __name__ == "__main__":
    __main__()
