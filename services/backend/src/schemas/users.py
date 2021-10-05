from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
  uid: str
  uname: str
  uemail: str
  upw: str

class User(UserBase):
  class Config():
    orm_mode = True


class ShowUser(BaseModel):
  uid: str
  uname: str
  uemail: str
  
  class Config():
    orm_mode = True
