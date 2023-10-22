from fastapi import FastAPI
from users.users import router as posts_router

app = FastAPI()

app.include_router(posts_router, prefix="/posts", tags=["posts"])
