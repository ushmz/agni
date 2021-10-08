from fastapi.routing import APIRouter
from domain.user import AuthedUserResponse, UserParam
from usecase.user import UserUsecase
from repository.user import UserRepositoryImpl

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
