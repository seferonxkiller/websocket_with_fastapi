from fastapi import FastAPI
from typing import List
from models import Post

app = FastAPI()

list = []
@app.get("/get")
async def get_posts():
    return {'name': list}


@app.get("/post{id}")
async def get_posts(post: Post):
    return {'id': post.id, 'name': post.name}


@app.post("/post_create")
async def post(post: Post):
    list.extend(post)
    return {'id': post.id, 'name': post.name}
