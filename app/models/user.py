from typing import Union
from pydantic import BaseModel


class UserParam(BaseModel):
    uid: str
    external_id: Union[str, None]
    passwd: str


class TokenResponse(BaseModel):
    token: str


class CompletionResponse(BaseModel):
    code: str
