from routers import task, user, log, serp
from fastapi import FastAPI

# from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(task.router)
app.include_router(log.router)
app.include_router(serp.router)


@app.get("/")
def say_hello():
    return {"hello": "Keep greeting to world forever."}
