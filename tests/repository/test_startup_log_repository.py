from loguru import logger

from python_boilerplate.repository.model.startup_log import StartupLog
from python_boilerplate.repository.startup_log_repository import save


def test_save() -> None:
    saved_startup_log: StartupLog
    try:
        saved_startup_log = save()
    except Exception as ex:
        assert False, f"{save} raised an exception {ex}"
    assert saved_startup_log is not None
    logger.info(f"Saved startup log, id: {saved_startup_log}")
