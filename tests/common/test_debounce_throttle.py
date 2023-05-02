from time import sleep

from loguru import logger
from pytest_mock import MockFixture

from python_boilerplate.common.debounce_throttle import debounce, throttle
from python_boilerplate.common.trace import async_trace, trace

times_for_debounce: int = 0
times_for_throttle: int = 0


def test_debounce(mocker: MockFixture) -> None:
    import tests

    spy = mocker.spy(tests.common.test_debounce_throttle, "debounce_function")
    call_count: int = 3
    while call_count > 0:
        debounce_function(call_count)
        call_count -= 1
    spy.assert_called()
    assert times_for_debounce == 1


def test_throttle(mocker: MockFixture) -> None:
    import tests

    spy = mocker.spy(tests.common.test_debounce_throttle, "throttle_function")
    call_count: int = 5
    try:
        while call_count > 0:
            throttle_function(call_count)
            call_count -= 1
            sleep(0.1)
    except Exception as ex:
        assert False, f"Failed to test throttle_function(). {ex}"
    spy.assert_called()
    assert times_for_throttle >= 2


@trace
@debounce(wait=1)
def debounce_function(a_int: int) -> None:
    global times_for_debounce
    times_for_debounce += 1
    logger.warning(
        f"'debounce_function' was called with {a_int}, times: {times_for_debounce}"
    )


@async_trace
@throttle(limit=0.25)
def throttle_function(a_int: int) -> None:
    global times_for_throttle
    times_for_throttle += 1
    logger.warning(
        f"'throttle_function' was called with {a_int}, times: {times_for_throttle}"
    )
