from pydantic.main import BaseModel


class TaskParam(BaseModel):
    task_id: int


class TaskInfo(BaseModel):
    title: str
    description: str
    query: str
    author_id: str
    search_url: str


class Serp(BaseModel):
    id: str
    title: str
    url: str
    snippet: str


class SerpResponse(BaseModel):
    task_id: str
    serps: list
