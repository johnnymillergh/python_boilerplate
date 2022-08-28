from loguru import logger

from python_boilerplate.repository.model.startup_log import StartupLog


@logger.catch
def save() -> StartupLog:
    """
    Save a new startup log.
    :return: a StartupLog object
    """
    startup_log: StartupLog = StartupLog()
    startup_log.save()
    return startup_log
