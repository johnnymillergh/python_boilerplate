from pathlib import Path

import pytest
from _pytest.nodes import Node
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
    node: Node = request.node
    profile_html_path = PROFILE_ROOT / f"{node.path.parent.relative_to(TESTS_ROOT)}"
    if not profile_html_path.exists():
        # If parents is false (the default), a missing parent raises FileNotFoundError.
        # If exist_ok is false (the default), FileExistsError is raised if the target directory already exists.
        profile_html_path.mkdir(parents=True, exist_ok=True)
    results_file = profile_html_path / f"{node.name}.html"
    with open(results_file, "w", encoding="utf-8") as f_html:
        f_html.write(profiler.output_html())
        logger.info(f"Generated profile result: [{results_file}]")