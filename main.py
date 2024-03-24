from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None


my_posts = [
    {"title": "Post 1", "content": "Content 1", "published": True, "id": 1},
    {"title": "Post 2", "content": "Content 2", "published": False, "id": 2},
]


@app.get("/")
def root():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post.dict())
    return {"data": "post"}
