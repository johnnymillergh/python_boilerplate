import logging
import sys

from python_boilerplate.function.python_boilerplate_function import fib
from python_boilerplate.messaging.sending_email import send_email

log = logging.getLogger("rotatingFileLogger")

if __name__ == "__main__":
    log.info(f"len(sys.argv) = {len(sys.argv)}, sys.argv: {sys.argv}")
    if len(sys.argv) == 1:
        log.warning("Arguments not provided, set n = 0 as default")
        n = int(0)
    else:
        n = int(sys.argv[1])
    log.info(f"n = {n}, type: {type(n)}")
    log.info(f"fib(n) = {fib(n)}")
