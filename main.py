from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = Treu


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.title)
    return {"data": "new post"}
