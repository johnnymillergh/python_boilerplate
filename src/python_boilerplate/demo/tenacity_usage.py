import logging
import random
from logging import INFO, WARNING
from typing import Final

from loguru import logger
from tenacity import (
    after_log,
    retry,
    retry_if_exception_type,
    retry_if_result,
    stop_after_attempt,
    wait_fixed,
)

from python_boilerplate.__main__ import startup
from python_boilerplate.common.trace import trace

SUCCESS_RANGE: Final = range(200, 300)
loging_logger: Final = logging.getLogger()


# https://tenacity.readthedocs.io/en/latest/
# https://jamesfheath.com/2020/07/python-library-tenacity.html


@retry(stop=stop_after_attempt(3), after=after_log(loging_logger, WARNING))
def exception_function_1() -> None:
    logger.warning("Mocking failure 1")
    raise RuntimeError("Failure message 1")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2), after=after_log(loging_logger, INFO))
def exception_function_2() -> None:
    logger.warning("Mocking failure 2")
    raise RuntimeError("Failure message 2")


@retry(
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type((ValueError, NotImplementedError)),
    after=after_log(loging_logger, WARNING),
)
def different_exceptions_possible(x: int) -> str:
    if x == 1:
        logger.error("IO Error because x is 1")
        raise ValueError("Value error because x is 1")
    if x == 2:
        logger.error("Not implemented error because x is 2")
        raise NotImplementedError("Not implemented error because x is 2")
    if x == 3:
        logger.error("Type Error because x is 3, won't retry")
        raise TypeError("Type error because x is 3")
    return "success"


@trace
def validate_code(result: int) -> bool:
    needs_retry = result not in SUCCESS_RANGE
    if needs_retry:
        logger.warning(f"The result = {result}, which is NOT 2xx code, needs_retry = {needs_retry}")
    else:
        logger.info(f"The result = {result}, which is 2xx code, needs_retry = {needs_retry}")
    return needs_retry


@trace
@retry(
    stop=stop_after_attempt(3),
    retry=retry_if_result(validate_code),
    after=after_log(loging_logger, WARNING),
)
def customized_retry_logic_function(input_int: int) -> int:
    random_int = random.randint(0, 200)
    result = input_int + random_int
    logger.info(f"input_int + random_int = {input_int} + {random_int} = {result}")
    return result


if __name__ == "__main__":
    startup()
    exception_function_2()
