from usecase.log import LogUsecase
from repository.log import LogRepositoryImple
from domain.log import ClickLog, TimeLog
from fastapi import APIRouter, status

router = APIRouter()


@router.post("/logs/click", status_code=status.HTTP_204_NO_CONTENT)
def post_click_log(task_id: int, param: ClickLog):
    repo = LogRepositoryImple()
    lu = LogUsecase(repo)
    lu.post_click_log(param)
    return


@router.post("/logs/time/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def post_time_log(user_id: int, param: TimeLog):
    repo = LogRepositoryImple()
    lu = LogUsecase(repo)
    lu.post_time_log(param)
    return
