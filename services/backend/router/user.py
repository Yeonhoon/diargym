from fastapi import FastAPI, APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ..sql_db import schemas, models, database
from ..router import authentication
from typing import List
from ..hashing.hash import Hash
import psycopg2 as pg


router = APIRouter(
    tags=['user']
)

conn = pg.connect(
    dbname='postgres', 
    user='postgres', 
    password='Zpflrjs94!', 
    port='5432')

cursor = conn.cursor()
connect_db = database.get_db
get_auth = Depends(authentication.get_current_user)
@router.get('/', status_code=status.HTTP_200_OK)
def show_users(db:Session=Depends(connect_db), 
                get_current_user: schemas.User = get_auth):
    # data = db.query(models.User).all()
    data = db.execute('select uid, uemail from users').fetchall()
    return data

@router.get('/{id}', status_code=status.HTTP_200_OK)
async def show_user(id:int, db:Session=Depends(connect_db)):
    # data = db.query(models.User).filter(models.User.uid==id).first()
    data = db.execute('select uid, uemail from users where uid = :uid',{'uid':id}).fetchone()
    return data

@router.get("/users/whoami", dependencies=[Depends(authentication.get_current_user)]
)
async def read_users_me(get_current_user=Depends(authentication.get_current_user)):
    return get_current_user


@router.post('/newuser', status_code=status.HTTP_201_CREATED)
async def create_user(request: schemas.User, db:Session=Depends(connect_db)):
    data = models.User(uname=request.name, 
                        uemail = request.email,
                        upw= Hash.produce_hash_password(request.password))
    db.add(data)
    db.commit()
    db.refresh(data)
    # response = RedirectResponse(url='/home')
    return data

@router.delete('/delete')
def delete_user(id: int, db:Session=Depends(connect_db)):
    data = db.query(models.User).filter(models.User.uid == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User id with {id} not found")
    data.delete(synchronize_session=False)
    db.commit()
    return f"User id {id} deleted"

@router.put('/update')
def update_user(id: int, request:schemas.User, db: Session=Depends(connect_db)):
    data = db.query(models.User).filter(models.User.id == id)
    if not data.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User id with {id} not found")
    data.update(request)
    db.commit()
    return f"User Id {id} has been updated!"