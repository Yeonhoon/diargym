from fastapi import APIRouter, Depends, status, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session

from ..repository import user

router = APIRouter(
  prefix="/user",
  tags=['user']
)
get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db:Session=Depends(get_db)):
  return user.create_user(request, db)

@router.get('/', response_model=List[schemas.ShowUser], status_code=status.HTTP_200_OK)
def show_all_users(db: Session=Depends(get_db)):
  return user.show_all(db)  

@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id:int, db:Session=Depends(get_db)):
  return user.show_one(id, db)

@router.put('/{id}',status_code= status.HTTP_200_OK)
def update_user(id:int, request: schemas.User, db:Session=Depends(get_db)):
  return user.update(id, db, request)