from time import sleep

from python_boilerplate.common.profiling import elapsed_time


@elapsed_time(level="WARNING")
def time_consuming_function() -> str:
    sleep(3)
    return "done execution"


def test_elapsed_time() -> None:
    try:
        result = time_consuming_function()
    except Exception as ex:
        assert False, f"`time_consuming_function()` raised an exception {ex}"
    assert result is not None
