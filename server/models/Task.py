from lib2to3.pgen2.token import OP
from pydantic import BaseModel
from typing import Optional

class TaskModel(BaseModel):
    id: Optional[int] = None
    title: str 
    created_at: Optional[str] = None
    updated: Optional[str] = None

class TaskModelGetResponse(BaseModel):
    status: str
    data: list[TaskModel]

class TaskModelPostResponse(BaseModel):
    status: str
    message: str
    data: TaskModel