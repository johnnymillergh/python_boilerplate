from datetime import datetime
from typing import List

from jinja2 import Environment, FileSystemLoader, select_autoescape

from python_boilerplate.function_collection import get_resources_dir

_env: Environment = Environment(
    loader=FileSystemLoader(f"{get_resources_dir()}/html_template"),
    autoescape=select_autoescape(["html"]),
)


def render_template(template_name: str, render_dict: dict) -> str:
    template = _env.get_template(template_name)
    return template.render(render_dict)


def render_template_example() -> str:
    render_dict: dict = {}
    dict_table_data: List[dict] = [
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
    return _env.get_template("template_example.html").render(render_dict)
