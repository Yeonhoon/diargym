from fastapi.param_functions import Depends
import psycopg2 as pg
from fastapi import APIRouter, status, Depends
from pydantic.main import BaseModel
from .. import oauth2

router = APIRouter(
  tags=['postgres']
)
conn = pg.connect(dbname='postgres', user='postgres',password='Zpflrjs94!', port='5432')
cursor = conn.cursor()



@router.get('/allusers')
def select_users():
  cursor.execute('select * from table1')
  df = cursor.fetchall()
  return df

@router.get('/auser')
def select_user(uid):
  cursor.execute('select * from table1 where uid=%s', uid)
  result = cursor.fetchone()
  return result  

@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_user(uname, uemail, upw):
  sql = "insert into table1 (uname, uemail, upw) values(%s, %s, %s)"
  cursor.execute(sql, (uname, uemail, upw))
  conn.commit()
