from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    location: str
    comments: int = 0


class CreatePost(PostBase):
    pass


class UpdatePost(PostBase):
    title: str
    content: str
    published: bool
    likes: int
    comments: int


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int
    gender: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    favorites: int = 0

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    likes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int
    gender: str
    is_active: bool = True


class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    password: str
    age: int
    gender: str
    is_active: bool


# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    is_active: bool = None
    is_verified: bool = None


class Like(BaseModel):
    post_id: int
    dir: conint(le=1)


class Favorite(BaseModel):
    post_id: int
    dir: conint(le=1)
