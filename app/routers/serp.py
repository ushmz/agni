from usecase.serp import SerpUsecase
from repository.serp import SerpRepositoryImpl
from domain.serp import SearchResult
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks/{task_id}/serp", response_model=List[SearchResult])
def get_serp(task_id: int, offset: int = 0):
    repo = SerpRepositoryImpl()
    su = SerpUsecase(repo)
    serp = su.get_serp(task_id, offset)
    return serp
