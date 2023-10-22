from typing import List

from fastapi import APIRouter, HTTPException, status

from models.users import User, UserCreate
from db import db

router = APIRouter()


@router.get("/")
async def all_users() -> List[User]:
    return list(db.users.values())


@router.get("/{id}")
async def get_id_user(id: int) -> User:
    try:
        return db.users[id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(name_create: UserCreate) -> User:
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **name_create.dict())
    db.users[new_id] = user
    return user


@router.delete("/delete_user", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int) -> None:
    try:
        db.users.pop(id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
