from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import uvicorn

from routes import tasks

app = FastAPI(
    title="FastAPI + API Rest",
    description="Simple API REST with FastAPI and PostgreSQL"
)

app.include_router(tasks.router)

register_tortoise(
    app,
    db_url="postgres://postgres:contraseña@db:5432/fastapi",
    modules={"models": ["database.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)