import psycopg2 as pg
from fastapi import APIRouter, status


router = APIRouter()
conn = pg.connect(dbname='postgres', user='postgres',password='Zpflrjs94!', port='5432')
cursor = conn.cursor()

@router.get('/test',tags=['postgres'])
def test():
  cursor.execute('select * from table1')
  df = cursor.fetchall()
  return df

@router.post('/inserttest', status_code=status.HTTP_201_CREATED,tags=['postgres'])
def inserttest(uname, uemail, upw):
  sql = "insert into table1 (uname, uemail, upw) values(%s, %s, %s)"
  cursor.execute(sql, (uname, uemail, upw))
  conn.commit()
