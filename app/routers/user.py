from starlette.responses import Response
from models.user import CompletionResponse, TokenResponse, UserParam
from fastapi import APIRouter

router = APIRouter()


@router.post("/signup", response_model=TokenResponse)
def signup(request: UserParam):
    return {"token": ""}


@router.post("/signin", response_model=TokenResponse)
def signin(request: UserParam):
    return {"token": ""}


@router.get("/user/{user_id}/code", response_model=CompletionResponse)
def fetch_completion_code(user_id: str):
    return {"code": user_id}


@router.post("/user/{user_id}/logs")
def post_log():
    return Response(status_code=204)
