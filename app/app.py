from routers import task, user, log, serp, auth
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

app.include_router(auth.router, prefix="/api/v1")
app.include_router(task.router, prefix="/api/v1")
app.include_router(serp.router, prefix="/api/v1")
app.include_router(user.router, prefix="/api/v1")
app.include_router(log.router, prefix="/api/v1")


@app.get("/")
def say_hello():
    return {"hello": "Keep greeting to world forever."}
