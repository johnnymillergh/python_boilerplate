from typing import Any

import pytest
from loguru import logger
from pydantic import ValidationError

from python_boilerplate.demo.pydantic_usage import User, UserDataClass


def test_deserialize_user_from_dict() -> None:
    user: User = User.parse_obj({"id": 123, "name": "James"})
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is None


def test_deserialize_user_from_dict_when_id_is_abc_then_raise_validation_error() -> (
    None
):
    user_dict: dict[str, Any] = {"id": "abc", "name": "James"}
    with pytest.raises(ValidationError) as exc_info:
        validated: User = User.validate(user_dict)
        logger.info(f"Validated user: {validated}")
    assert exc_info.type == ValidationError
    logger.info(f"Exception raised during validation. {exc_info.value}")


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


def test_initialize_user_with_dataclass() -> None:
    user: UserDataClass = UserDataClass(id=1, name="John")
    assert user is not None
    assert user.id == 1
    assert user.name == "John"
    logger.info(f"{user}")
