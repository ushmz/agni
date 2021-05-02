from models import task
from fastapi import APIRouter

router = APIRouter()


@router.get("/task/{task_id}")
def fetch_task_info(task_id: str):
    return {
        "title": "",
        "description": "",
        "query": "",
        "author_id": "",
        "search_url": "",
    }


@router.post("/tasks")
def post_answer(request: task.TaskParam):
    return {"id": 1}


@router.get("/serp/{task_id}", response_model=task.SerpResponse)
def fetch_serp_by_id(task_id: str):
    return {
        "task_id": task_id,
        "serps": [
            {
                "id": "1",
                "title": "Dummy title",
                "url": "http://example.com",
                "snippet": "Sample snippet",
            },
            {
                "id": "2",
                "title": "Dummy title",
                "url": "http://example.com",
                "snippet": "Sample snippet",
            },
        ],
    }
