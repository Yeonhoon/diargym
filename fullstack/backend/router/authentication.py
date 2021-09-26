from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from ..sql_db import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing.hash import Hash
router = APIRouter()

@router.post('/login')
def login(request: schemas.Login, db: Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.uemail == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"등록되지 않은 회원입니다.")
    if not Hash.verify_password(user.upw, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="올바르지 않은 비밀번호입니다")
    else:
        return user