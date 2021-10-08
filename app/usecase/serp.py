from domain.task import SearchResult
from typing import List


class SerpUsecase:
    def __init__(self, repository) -> None:
        self.repository = repository

    def get_serp(self, task_id: int, offset: int) -> List[SearchResult]:
        return self.repository.get_serp(task_id, offset)
