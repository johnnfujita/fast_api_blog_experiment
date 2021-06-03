from pydantic import BaseModel
from typing import List, Optional 


class _UserLogin(BaseModel):
    username: str
    password: str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode =True


class _User(BaseModel):
    name: str
    email: str
    password: str
    

class _UserShow(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog] = []
    class Config():
        orm_mode =True
class User_Little(BaseModel):
    name: str
    class Config():
        orm_mode =True

class Blog(BaseModel):
    title: str
    body: str
    creator: User_Little
    class Config():
        orm_mode =True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None