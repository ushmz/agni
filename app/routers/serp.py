from usecase.serp import SerpUsecase
from repository.serp import SerpRepositoryImpl
from domain.task import SearchResult
from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/serp/{task_id}", response_model=List[SearchResult])
def get_serp(task_id: int, offset: int = 0):
    repo = SerpRepositoryImpl()
    su = SerpUsecase(repo)
    serp = su.get_serp(task_id, offset)
    return serp
