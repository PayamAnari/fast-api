from pydantic import BaseModel, EmailStr
from datetime import datetime


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


class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int
    is_active: bool = True
    gender: str


class UserOut(BaseModel):
    username: str
    email: EmailStr
    age: int
    is_active: bool
    gender: str
    created_at: datetime

    class Config:
        orm_mode = True
