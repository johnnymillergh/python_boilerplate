from python_boilerplate.repository.model.trace_log import TraceLog
from python_boilerplate.repository.trace_log_repository import retain_trace_log, save


def test_save() -> None:
    try:
        saved = save(
            TraceLog(
                called_by="test_caller",
                function_qualified_name=test_save.__qualname__,
                function_arguments="[]",
            )
        )
    except Exception as ex:
        assert False, f"{save} raised an exception {ex}"
    assert saved is not None


def test_retain_trace_log():
    try:
        retain_trace_log()
    except Exception as ex:
        assert False, f"{retain_trace_log} raised an exception {ex}"
