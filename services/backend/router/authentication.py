from fastapi import FastAPI, APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from ..sql_db import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing.hash import Hash
from ..hashing import JWTtoken

router = APIRouter(
    tags=['Authentication']
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), 
        db: Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.uemail == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"등록되지 않은 회원입니다.")
    if not Hash.verify_password(user.upw, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="올바르지 않은 비밀번호입니다")

    # JWT Token: data(email)을 받아 토큰화된 정보를 통해 로그인 하기
    # token을 통해 authentication을 받은 유저만 사용할 수 있게끔 하는 것.
    # login을 진행한 유저는 id가 아닌 token 형태로 보이게 됨.
    access_token = JWTtoken.create_access_token(data={"sub":user.uemail})
    return {'access_token':access_token, 'token_type': 'bearer'}


def get_current_user(token: str= Depends(oauth2_scheme)):
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="증명되지 않은 사용자입니다.",
    headers={'WWW-Authenticate':'Bearer'}
  )
  
  return JWTtoken.verify_token(token, credentials_exception)