from fastapi import APIRouter

router = APIRouter(
    tags=["Tasks"],
    prefix="/api/tasks"
)

@router.get("/")
async def get_tasks():
    return ""