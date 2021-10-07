from domain.task import Answer, Task
from domain.repository.task import TaskRepository


class TaskRepositoryImpl(TaskRepository):
    def get_task_description(self, task_id: int) -> Task:
        """
        Get task information (title, descriptions, etc...)

        args:
            task_id(int) : Task id that you'd like to fetch
        returns:
            info(TaskInfo) : Information object
        """
        raise NotImplementedError(f"params: task_id={task_id}")

    def create_answer(self, answer: Answer) -> None:
        """
        Insert user's answer to DB

        args:
            answer(Answer) : User's task answer and reason
        returns:
            None
        """
        raise NotImplementedError(f"params: answer={answer}")
