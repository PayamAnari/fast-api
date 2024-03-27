from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    likes: int = 0
    comments: int = 0
