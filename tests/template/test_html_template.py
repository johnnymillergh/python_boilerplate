from loguru import logger

from python_boilerplate.template.html_template import render_template_example


def test_render_template_example() -> None:
    rendered = render_template_example()
    logger.info(f"Rendered template: \n{rendered}")
    assert rendered is not None
