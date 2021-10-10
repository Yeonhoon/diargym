from fastapi.param_functions import Query
from pydantic import BaseModel
from pydantic.fields import ModelField
from typing import List, Optional, Type
from datetime import date, datetime
from fastapi import Form
import inspect
from sqlalchemy.sql import annotation


class RecordBase(BaseModel):
    # ruserid: str
    rdate: str
    rlarge: str
    rmid: str
    rsmall: str
    rweight: str
    runit: str
    rrep: str

    # def __init__(self, rdate:str=Form(...), rlarge:str=Form(...), rmid:str=Form(...),
    #                     rsmall:str=Form(...), rweight:float=Form(...), runit: str=Form(...),
    #                     rrep: int=Form(...)):
    #     super().__init__(rdate, rlarge, rmid, rsmall, rweight, runit, rrep)


class Record(RecordBase):
  class Config():
    orm_mode = True


class ShowRecord(BaseModel):
    ruser: str
    rdate: date
  
    class Config():
      orm_mode = True


