from typing import Union
from pydantic import BaseModel


class UserParam(BaseModel):
    uid: str
    external_id: Union[str, None]
    # passwd: str


class UserSimple(BaseModel):
    uid: str
    external_id: str
    condition_id: int
    # allocated_task?


class TokenResponse(BaseModel):
    token: str


class CompletionResponse(BaseModel):
    code: str


class AuthedUserResponse(BaseModel):
    token: str
    user: UserSimple
