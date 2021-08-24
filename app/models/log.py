from pydantic.main import BaseModel


class BehaviorLog(BaseModel):
    id: int
    uid: int
    click_count: int
    time_on_page: int
    referrer: str
    refocus_count: int
    url: str
    task_id: int
    condition_id: int
