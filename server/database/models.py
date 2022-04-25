from tortoise import fields
from tortoise.models import Model

class Task(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "tasks"