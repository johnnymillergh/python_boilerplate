from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: Optional[datetime]


@dataclass
class UserDataClass:
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
