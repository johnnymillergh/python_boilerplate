from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class User(BaseModel):
    id: int
    name: str = "John Doe"
    # signup_ts is not required, can be None
    signup_ts: datetime | None = None


@dataclass
class UserDataClass:
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
