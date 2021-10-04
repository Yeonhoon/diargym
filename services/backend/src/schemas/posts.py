from pydantic import BaseModel
from typing import List, Optional

class PostBase(BaseModel):
    pid: int
    ptitle: str
    pcontent: str
    author: str


class Post(PostBase):
  class Config():
    orm_mode = True


class ShowPost(BaseModel):
    pid: int
    ptitle: str
    pcontent: str
    author: str

  
    class Config():
      orm_mode = True
