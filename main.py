from fastapi import FastAPI, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None


my_posts = [
    {
        "title": "Post 1",
        "content": "Content 1",
        "published": True,
        "rating": 5,
        "id": 1,
    },
    {
        "title": "Post 2",
        "content": "Content 2",
        "published": False,
        "rating": 4,
        "id": 2,
    },
]


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"message": "Post successfully created", "data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):

    if id < 1 or id > len(my_posts):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    post = my_posts[id - 1]
    return {"data": post}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    my_posts[id - 1] = post.dict()
    return {"data": my_posts[id - 1]}


@app.delete("/posts/{id}")
def delete_post(id: int):
    my_posts.pop(id - 1)
    return {"message": "Post successfully deleted", "data": my_posts}
