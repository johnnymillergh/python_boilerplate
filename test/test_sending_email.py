from python_boilerplate.messaging.sending_email import build_message


def test_build_message():
    message = build_message("Test")
    assert message.as_string() is not None
