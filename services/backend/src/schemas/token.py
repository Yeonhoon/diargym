from typing import Optional

from pydantic import BaseModel


class TokenData(BaseModel):
    uname: Optional[str] = None


class Status(BaseModel):
    message: str