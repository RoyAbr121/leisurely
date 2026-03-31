from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel

from src.core.celery_app import celery_app
from src.tasks.example import add, send_welcome_email

app = FastAPI(title="Leisurely")


class AddRequest(BaseModel):
    x: int
    y: int


class EmailRequest(BaseModel):
    email: str
    username: str


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/tasks/add")
async def dispatch_add(payload: AddRequest):
    task = add.delay(payload.x, payload.y)
    return {"task_id": task.id}


@app.post("/tasks/email")
async def dispatch_email(payload: EmailRequest):
    task = send_welcome_email.delay(payload.email, payload.username)
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.successful() else None,
    }
