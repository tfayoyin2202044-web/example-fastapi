from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# 1. Base Schemas
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# 2. Output Schemas
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# Define full Post BEFORE PostOut
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

# Inherit from BaseModel (NOT PostBase), since the query wraps Post and votes
class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

# 3. Auth & Vote Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)