from fastapi import APIRouter, status, HTTPException
from fastapi.encoders import jsonable_encoder

from database.models import Task
from models.Task import TaskModel, TaskModelGetResponse, TaskModelPostResponse

router = APIRouter(
    tags=["Tasks"],
    prefix="/api/tasks"
)

@router.get("/", status_code=status.HTTP_200_OK, description="Get all tasks", response_model=TaskModelGetResponse)
async def get_tasks():
    tasks: list[Task] = await Task.all()

    response = jsonable_encoder({
        "status": "success",
        "data": tasks
    })

    return response

@router.get("/:id", status_code=status.HTTP_200_OK)
async def get_task(id: int):
    try:
        task: Task = await Task.get(id=id)
    except:
        response = jsonable_encoder({
            "status": "error",
            "message": "Task not found"
        })
        raise HTTPException(detail=response, status_code=status.HTTP_404_NOT_FOUND)

    response = jsonable_encoder({
        "status": "success",
        "data": task
    })

    return response

@router.post("/", status_code=status.HTTP_201_CREATED, description="Create a new task", response_model=TaskModelPostResponse)
async def create_task(task: TaskModel):
    new_task = await Task.create(title=task.title)

    response = jsonable_encoder({
        "status": "success",
        "message": "Task created",
        "data": new_task
    })

    return response