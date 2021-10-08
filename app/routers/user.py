from usecase.user import UserUsecase
from repository.user import UserRepositoryImpl
from domain.user import AuthedUserResponse, CompletionResponse
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}", response_model=AuthedUserResponse)
def get_user(user_id: int):
    return {"token": "", "user": {}}


@router.get("/users/{user_id}/code", response_model=CompletionResponse)
def fetch_completion_code(user_id: int):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    code = uu.get_completion_code(user_id)
    return {"code": code}
