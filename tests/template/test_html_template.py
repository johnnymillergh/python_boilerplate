from datetime import datetime
from typing import Any

from loguru import logger

from python_boilerplate.template.html_template import render_template


def test_render_template_when_the_template_exists_then_no_raised_exception() -> None:
    render_dict: dict[str, Any] = {}
    dict_table_data: list[dict[str, Any]] = [
        {"Name": "Basketball", "Type": "Sports", "Value": 5},
        {"Name": "Football", "Type": "Sports", "Value": 4.5},
        {"Name": "Pencil", "Type": "Learning", "Value": 5},
        {"Name": "Hat", "Type": "Wearing", "Value": 2},
    ]
    render_dict.update(
        {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "content": "Hello reader, here is a table:",
            "content_id": "cid:a_picture_id",
            "array_table_head": ["Name", "Type", "Value"],
            "dict_table_data": dict_table_data,
        }
    )
    try:
        rendered = render_template("template_example.html", render_dict)
    except Exception as ex:
        assert False, f"Could not render template. {ex}"
    assert rendered is not None
    assert len(rendered) > 0
    assert "Basketball" in rendered
    assert "Hello reader, here is a table" in rendered
    assert "cid:a_picture_id" in rendered
    logger.info(f"Rendered template: \n{rendered}")
