# models.py
from bson import ObjectId
from pydantic import BaseModel, validator

class User(BaseModel):
    id: str
    name: str
    email: str
