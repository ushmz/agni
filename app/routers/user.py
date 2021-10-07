from usecase.user import UserUsecase
from repository.user import UserRepositoryImpl
from domain.user import AuthedUserResponse, CompletionResponse, UserParam
from fastapi import APIRouter

router = APIRouter()


@router.post("/signup", response_model=AuthedUserResponse)
def signup(req: UserParam):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    user = uu.create_user(req)
    return {"token": "", "user": user}


@router.post("/signin", response_model=AuthedUserResponse)
def signin(req: UserParam):
    return {"token": "", "user": {}}


@router.get("/code/user/{user_id}", response_model=CompletionResponse)
def fetch_completion_code(user_id: int):
    repo = UserRepositoryImpl()
    uu = UserUsecase(repo)
    code = uu.get_completion_code(user_id)
    return {"code": code}
