from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse, Response
from starlette.status import HTTP_201_CREATED
from .sql_db import models,database, schemas

import psycopg2 as pg
app = FastAPI( )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.29.114.158:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conn = pg.connect(
    dbname='postgres', 
    user='postgres', 
    password='Zpflrjs94!', 
    port='5432')

cursor = conn.cursor()
connect_db = database.get_db

# @app.get('/')
# def get_all():
#     sql = 'select uid, uname, uemail, upw from table1';
#     cursor.execute(sql);
#     df = cursor.fetchall()
#     return df
@app.get('/home')
def mainPage():
    pass

@app.get('/')
def get_all2(db:Session=Depends(connect_db)):
    data = db.query(models.User).all()
    return data

@app.post('/newuser', status_code=HTTP_201_CREATED)
async def create_user(request: schemas.User, db:Session=Depends(connect_db)):
    data = models.User(uname=request.name, 
                        uemail = request.email,upw=request.password)
    db.add(data)
    db.commit()
    db.refresh(data)
    # response = RedirectResponse(url='/home')
    return data

@app.delete('/delete')
def delete_user(id: int, db:Session=Depends(connect_db)):
    data = db.query(models.User).filter(models.User.uid == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User id with {id} not found")
    data.delete(synchronize_session=False)
    db.commit()
    return f"User id {id} deleted"

@app.put('/update')
def update_user(id: int, request:schemas.User, db: Session=Depends(connect_db)):
    data = db.query(models.User).filter(models.User.id == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User id with {id} not found")
    data.update(request)
    db.commit()
    return f"User Id {id} has been updated!"

