from repository.task import TaskRepositoryImpl
from usecase.task import TaskUsecase
from fastapi import APIRouter
from domain.task import Answer, Task

router = APIRouter()


@router.get("/tasks/{task_id}", response_model=Task)
def fetch_task_description(task_id: int) -> Task:
    repo = TaskRepositoryImpl()
    task = TaskUsecase(repo).get_task_description(task_id)
    return task


@router.post("/tasks/{task_id}/answer")
def save_answer(task_id: int, answer: Answer) -> None:
    repo = TaskRepositoryImpl()
    TaskUsecase(repo).save_task_answer(task_id, answer)
    return
