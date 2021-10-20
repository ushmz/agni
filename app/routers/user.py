from starlette import status
from starlette.responses import Response
from usecase.orm.user import UserUsecase
from repository.orm.user import UserRepositoryImpl
from domain.user import (
    AuthedUserResponse,
    CompletionCodeParam,
    CompletionResponse,
    UserParam,
)
from fastapi import APIRouter

router = APIRouter()


@router.post("/users", response_model=AuthedUserResponse)
def create_user(param: UserParam):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    user = uu.create_user(param)
    return {"token": "", "user": user}


@router.get("/users/{user_id}", response_model=AuthedUserResponse)
def get_user(user_id: int):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    user = uu.get_user(user_id)
    return {"token": "", "user": user}


@router.post("/users/{user_id}/code", status_code=status.HTTP_204_NO_CONTENT)
def set_completion_code(param: CompletionCodeParam):
    """This endpoint should not be exposed, perhaps."""
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    uu.set_completion_code(param.user, param.code)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/users/{user_id}/code", response_model=CompletionResponse)
def fetch_completion_code(user_id: int):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    code = uu.get_completion_code(user_id)
    return {"code": code}
