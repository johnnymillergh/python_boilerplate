from time import sleep

from apscheduler.triggers.cron import CronTrigger
from loguru import logger
from pytest_mock import MockerFixture, MockFixture

from python_boilerplate.configuration.apscheduler_configuration import (
    cleanup,
    configure,
    scheduler,
)


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        assert False, f"{configure} raised an exception {ex}"


@scheduler.scheduled_job(trigger=CronTrigger.from_crontab("* * * * *"))
def timed_job() -> None:
    logger.info("This is a timed job")


def test_scheduler_when_adding_in_interval_job(mocker: MockFixture) -> None:
    if not scheduler.running:
        scheduler.start()
    import tests

    spy = mocker.spy(tests.configuration.test_apscheduler_configuration, "timed_job")
    try:
        scheduler.add_job(func=timed_job, trigger="interval", seconds=1)
        sleep(5)
    except Exception as ex:
        assert False, f"{scheduler} raised an exception. {ex}"
    assert spy.call_count <= 5


def test_cleanup(mocker: MockerFixture) -> None:
    # pytest-mock, patch an object, https://pytest-mock.readthedocs.io/en/latest/usage.html
    executor_patch = mocker.patch.object(scheduler, "shutdown")
    cleanup()
    executor_patch.assert_called_once()
