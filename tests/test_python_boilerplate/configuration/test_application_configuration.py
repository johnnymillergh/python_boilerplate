import pytest

from python_boilerplate.configuration.application_configuration import configure


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        pytest.fail(f"{configure} raised an exception {ex}")
