# models.py
from bson import ObjectId
from pydantic import BaseModel, validator

class Task(BaseModel):
    id: str
    owner_id: str
    title: str
    description: str