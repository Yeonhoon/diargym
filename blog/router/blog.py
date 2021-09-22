from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
  prefix="/blogs",
  tags=['blogs']

)
get_db = database.get_db
 
@router.get('/', response_model=List[schemas.ShowBlog], )
def all(db: Session=Depends(get_db)):
  return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED , )
def create(request: schemas.Blog, db:Session=Depends(get_db)):
 return blog.create_post(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,)
def remove(id, db:Session=Depends(get_db)):
  blog=db.query(models.Blog).filter(models.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"blog id with {id} not found")
  blog.delete(synchronize_session=False)
  db.commit()
  return 'Deleted'


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, )
def update(id, request: schemas.Blog, db:Session=Depends(get_db)):
  blog=db.query(models.Blog).filter(models.Blog.id == id)
  if not blog.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Blog id with {id} not found")
  blog.update(request)
  db.commit()
  return 'update success'


@router.get('/', response_model=List[schemas.ShowBlog], ) # response model: response를 어떻게 할 것인지 타입 정해줌.
def all(db:Session=Depends(get_db)):
  blogs = db.query(models.Blog).all()
  return blogs

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog, )
def show_single(id,response:Response, db:Session=Depends(get_db)):
  blog = db.query(models.Blog).filter(models.Blog.id == id).first()
  if not blog:
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'detail':f'Blog with {id} is not available'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Blog with {id} is not available")
  return blog