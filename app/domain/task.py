from pydantic.main import BaseModel


class TaskParam(BaseModel):
    task_id: int


class Task(BaseModel):
    title: str
    description: str
    query: str
    author_id: str
    search_url: str


class SearchResult(BaseModel):
    id: str
    title: str
    url: str
    snippet: str


class SerpResponse(BaseModel):
    task_id: str
    serps: list


class Answer(BaseModel):
    task_id: int
    answer: str
    reason: str