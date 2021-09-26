from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
  title: str
  content: str

class UserBase(BaseModel):
  name: str
  email: str
  password: str

class User(UserBase):
  class Config():
    orm_mode = True

class Blog(BlogBase):
  class Config():
    orm_mode = True

class ShowUser(BaseModel):
  name: str
  email: str
  
  class Config():
    orm_mode = True

class Login(BaseModel):
  email: str
  password: str