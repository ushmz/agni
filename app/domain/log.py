from pydantic.main import BaseModel


class BehaviorLog(BaseModel):
    uid: int
    click_count: int
    time_on_page: int
    referrer: str
    refocus_count: int
    url: str
    task_id: int
    condition_id: int


class ClickLog(BaseModel):
    user_id: int
    task_id: int
    condition_id: int
    url: str
    referrer: str


class TimeLog(BaseModel):
    user_id: int
    task_id: int
    condition_id: int
