from urllib import response
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder

from database.models import Task
from models.Task import TaskModel

router = APIRouter(
    tags=["Tasks"],
    prefix="/api/tasks"
)

@router.get("/", status_code=status.HTTP_200_OK, description="Get all tasks")
async def get_tasks():
    tasks = await Task.all()

    response = jsonable_encoder({
        "status": "success",
        "data": tasks
    })

    return response

@router.post("/", status_code=status.HTTP_201_CREATED, description="Create a new task")
async def create_task(task: TaskModel):
    new_task = await Task.create(title=task.title)

    response = jsonable_encoder({
        "status": "success",
        "message": "Task created",
        "data": new_task
    })

    return response