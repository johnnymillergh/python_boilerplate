from loguru import logger

from python_boilerplate.demo.pydantic_usage import User


def test_deserialize_user_from_dict() -> None:
    user: User = User.parse_obj({"id": 123, "name": "James"})
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is None


def test_deserialize_user_from_json() -> None:
    user: User = User.parse_raw('{"id": 123, "name": "James"}')
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is None


def test_deserialize_user_from_json_when_signup_ts_is_provided() -> None:
    user: User = User.parse_raw(
        '{"id": 123, "name": "James", "signup_ts": "2023-01-01 00:00:00"}'
    )
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is not None
    logger.info(f"User: {user}, user in JSON: {user.json()}")
