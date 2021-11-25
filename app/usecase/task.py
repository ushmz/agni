from domain.task import Answer, Task
from domain.repository.task import TaskRepository


class TaskUsecase:
    def __init__(self, repository: TaskRepository) -> None:
        self.repository = repository

    def get_task_description(self, task_id: int) -> Task:
        task = self.repository.get_task_description(task_id)
        return task

    def save_task_answer(self, answer: Answer) -> int:
        ans_id = self.repository.create_answer(answer)
        return ans_id
