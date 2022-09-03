from jinja2 import Environment, FileSystemLoader, select_autoescape

from python_boilerplate.function_collection import get_resources_dir

_ENVIRONMENT: Environment = Environment(
    loader=FileSystemLoader(get_resources_dir() / "html_template"),
    autoescape=select_autoescape(["html"]),
)


def render_template(template_name: str, render_dict: dict) -> str:
    """
    Render template.

    :param template_name: the name of the template
    :param render_dict: the dictionary
    """
    template = _ENVIRONMENT.get_template(template_name)
    return template.render(render_dict)
