from fastapi.param_functions import Query
from pydantic import BaseModel
from pydantic.fields import ModelField
from typing import List, Optional, Type
from datetime import date, datetime
from fastapi import Form
import inspect

# from sqlalchemy.sql import annotation


class RecordBase(BaseModel):
    rdate: str
    rsmall: str
    rweight: str
    runit: str
    rrep: str


class Record(RecordBase):
  class Config():
    orm_mode = True


class ShowRecord(RecordBase):
    ruserid:str
    rdate: str
    rsmall: str
    rweight: str
    runit: str
    rrep: str
  
    class Config():
      orm_mode = True


