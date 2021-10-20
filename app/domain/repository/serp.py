from abc import ABCMeta, abstractmethod
from domain.serp import SearchResult
from typing import List


class SerpRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_serp(self, task_id: int, offset: int) -> List[SearchResult]:
        """
        Get search result pages by given task INIT_DB

        args:
            task_id(int) : Task ID
        returns:
            serps(List[Serp]) : Listed result page objects
        """
        raise NotImplementedError(f"params: task_id={task_id}")
