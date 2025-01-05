from typing import Any

import pytest
from loguru import logger
from pydantic import ValidationError
from pytest_benchmark.fixture import BenchmarkFixture

from python_boilerplate.demo.pydantic_usage import User, UserDataClass


def test_deserialize_user_from_dict() -> None:
    user: User = User.model_validate({"id": 123, "name": "James", "signup_ts": None})
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is None
    user_json_excluded_none = user.model_dump_json(exclude_none=True)
    user_json_included_none = user.model_dump_json()
    assert len(user_json_excluded_none) > 0
    assert len(user_json_included_none) > 0
    assert len(user_json_excluded_none) < len(user_json_included_none)
    assert "signup_ts" not in user_json_excluded_none
    assert "signup_ts" in user_json_included_none
    logger.info(f"User (excluded none): {user_json_excluded_none}, user (includes none): {user_json_included_none}")


def test_deserialize_user_from_dict_when_id_is_abc_then_raise_validation_error() -> None:
    user_dict: dict[str, Any] = {"id": "abc", "name": "James"}
    with pytest.raises(ValidationError, match="abc") as exc_info:
        User.model_validate(user_dict)
    assert exc_info.type == ValidationError
    logger.info(f"Exception raised during validation. {exc_info.value}")


def test_deserialize_user_from_json() -> None:
    user: User = User.model_validate_json('{"id": 123, "name": "James"}')
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is None


def test_deserialize_user_from_json_when_signup_ts_is_provided() -> None:
    user: User = User.model_validate_json('{"id": 123, "name": "James", "signup_ts": "2023-01-01 00:00:00"}')
    assert user is not None
    assert user.id == 123
    assert user.name == "James"
    assert user.signup_ts is not None
    logger.info(f"User: {user}, user in JSON: {user.model_dump_json()}")


def test_initialize_user_with_dataclass() -> None:
    user: UserDataClass = UserDataClass(id=1, name="John")
    assert user is not None
    assert user.id == 1
    assert user.name == "John"
    assert user.signup_ts is None
    logger.info(f"{user}")


def create_instance() -> User:
    return User.model_validate({"id": 123, "name": "James"})


def serialize_instance() -> str:
    return User.model_validate({"id": 123, "name": "James"}).model_dump_json()


def test_create_instance_benchmark(benchmark: BenchmarkFixture) -> None:
    benchmark(create_instance)


def test_serialize_instance_benchmark(benchmark: BenchmarkFixture) -> None:
    benchmark(serialize_instance)
