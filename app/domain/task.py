from pydantic.main import BaseModel


class TaskParam(BaseModel):
    task_id: int


class Task(BaseModel):
    title: str
    query: str
    description: str
    search_url: str


class Answer(BaseModel):
    user_id: int
    task_id: int
    condition_id: int
    answer: str
    reason: str
