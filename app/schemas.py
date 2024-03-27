from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    likes: int = 0
    comments: int = 0


class CreatePost(PostBase):
    pass


class UpdatePost(PostBase):
    title: str
    content: str
    published: bool
    likes: int
    comments: int
