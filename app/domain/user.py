from typing import List
from pydantic import BaseModel


class UserParam(BaseModel):
    external_id: str
    # passwd: str


class UserSimple(BaseModel):
    id: int
    external_id: str
    condition: int
    tasks: List[int]


class TokenResponse(BaseModel):
    token: str


class CompletionCodeParam(BaseModel):
    user: int
    code: int


class CompletionResponse(BaseModel):
    code: str


class AuthedUserResponse(BaseModel):
    token: str
    user: UserSimple
