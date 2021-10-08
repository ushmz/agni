from domain.task import SearchResult
from typing import List
from domain.repository.serp import SerpRepository


class SerpRepositoryImpl(SerpRepository):
    def get_serp(self, task_id: int, offset: int) -> List[SearchResult]:
        """
        Get search result pages by given task INIT_DB

        args:
            task_id(int) : Task ID
        returns:
            serps(List[Serp]) : Listed result page objects
        """
        raise NotImplementedError(f"params: task_id={task_id}, offset={offset}")
