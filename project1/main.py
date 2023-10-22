from fastapi import FastAPI
from typing import Optional
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI(title="Project1")


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = []


@app.get("/posts")
async def get_posts():
    return {"data": "sdfsdf"}


@app.post("/createposts")
async def create_post(new_post: Post):
    print(new_post.title)
    print(new_post.dict())
    return {"post_name": new_post.title, "post_content": new_post.content}
