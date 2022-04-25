from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routes import tasks

app = FastAPI()

app.include_router(tasks.router)

register_tortoise(
    app,
    db_url="postgres://postgres:contraseña@localhost:5432/fastapi",
    modules={"models": ["models.models"]},
    generate_schemas=True,
    add_exception_handlers=True
)