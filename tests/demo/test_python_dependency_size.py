from python_boilerplate.demo.python_dependency_size import list_python_dependencies


def test_list_python_dependencies() -> None:
    try:
        list_python_dependencies()
    except Exception as e:
        assert False, f"Failed to test throttle_function(). {e}"
