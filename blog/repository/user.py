from sqlalchemy.orm import Session
from ..import models, schemas
from fastapi import HTTPException, status
from ..hashing import Hash


def create_user(request:schemas.User, db:Session):
  new_user = models.User(name=request.name, 
                email = request.email, 
                password = Hash.bcrypt(request.password))
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def show_all(db:Session):
  users = db.query(models.User).all()
  return users


def show_one(id: int, db: Session):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"USER ID {id} not found")
  return user


def update(id: int, request:schemas.User, db:Session):
  user = db.query(models.User).filter(models.User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User id with {id} not found")
  user.update(request)
  db.commit()
  return 'update success'