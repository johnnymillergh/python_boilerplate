from pathlib import Path

import pytest
from loguru import logger
from pyinstrument import Profiler

TESTS_ROOT = Path.cwd()


@pytest.fixture(autouse=True)
def auto_profile(request):
    """
    Generate a HTML file for each test node in your test suite inside the .profiles directory.

    https://pyinstrument.readthedocs.io/en/latest/guide.html#profile-pytest-tests
    """

    # noinspection PyPep8Naming
    PROFILE_ROOT = TESTS_ROOT / ".profiles"
    logger.info("Starting to profile Pytest unit tests...")
    # Turn profiling on
    profiler = Profiler()
    profiler.start()

    yield  # Run test

    profiler.stop()
    PROFILE_ROOT.mkdir(exist_ok=True)
    results_file = PROFILE_ROOT / f"{request.node.name}.html"
    with open(results_file, "w", encoding="utf-8") as f_html:
        f_html.write(profiler.output_html())
        logger.info(f"Generated result: [{results_file}]")
