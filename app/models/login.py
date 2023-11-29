
from pydantic import BaseModel

from typing import Union


class LoginModel(BaseModel):
    username: str
    password: str


class TokenModel(BaseModel):
    access_token: str
    token_type: str


class TokenDataModel(BaseModel):
    username: Union[str, None] = None
