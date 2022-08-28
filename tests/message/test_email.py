from python_boilerplate.message.email import __init__, cleanup


def test_init() -> None:
    try:
        __init__()
    except Exception as ex:
        assert False, f"{__init__} raised an exception {ex}"


def test_cleanup() -> None:
    try:
        cleanup()
    except Exception as ex:
        assert False, f"{cleanup} raised an exception {ex}"
