from pydantic import BaseModel
from uuid import UUID
from fastapi import Body


class Post(BaseModel):
    id: int
    name: str = Body(..., min_length=2, max_length=10)
    