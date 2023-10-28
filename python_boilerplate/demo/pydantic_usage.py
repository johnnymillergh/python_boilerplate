from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class User(BaseModel):
    id: int
    name: str = "John Doe"
    # signup_ts is not required, can be None
    signup_ts: Optional[datetime] = None


@dataclass
class UserDataClass:
    id: int
    name: str = "John Doe"
    signup_ts: Optional[datetime] = None
