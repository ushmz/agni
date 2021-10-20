from pydantic.main import BaseModel


class SearchResult(BaseModel):
    id: str
    title: str
    url: str
    snippet: str


class SerpResponse(BaseModel):
    task_id: str
    serps: list
