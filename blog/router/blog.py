from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
  prefix="/blogs",
  tags=['blogs']

)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db),
    current_user: schemas.User=Depends(oauth2.get_current_user)):
  return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED )
def create(request: schemas.Blog, db:Session=Depends(get_db),
    current_user: schemas.User=Depends(oauth2.get_current_user)):
 return blog.create_post(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,)
def remove(id: int, db:Session=Depends(get_db),
    current_user: schemas.User=Depends(oauth2.get_current_user)):
  return blog.destroy(id, db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, )
def update(id: int, request: schemas.Blog, db:Session=Depends(get_db),
    current_user: schemas.User=Depends(oauth2.get_current_user)):
  return blog.update(id, request, db)


# @router.get('/', response_model=List[schemas.ShowBlog], ) # response model: response를 어떻게 할 것인지 타입 정해줌.
# def all(db:Session=Depends(get_db)):
#   blogs = db.query(models.Blog).all()
#   return blogs

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog, )
def show_single(id, db:Session=Depends(get_db),
    current_user: schemas.User=Depends(oauth2.get_current_user)):
  return blog.show(id, db)