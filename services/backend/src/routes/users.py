from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.routing import Router
from src.crud import users as crud
from src.auth.users import validate_user, get_user
from src.auth.jwthandler import create_access_token
from src.schemas.token import Status
from src.schemas.users import ShowUser, User
from src.database.models import get_db

from src.auth.jwthandler import (
    create_access_token,
    get_current_user
)

connect_db = get_db

router = APIRouter(
  tags=['users']
)

@router.get('/getuser/{uid}')
async def get_a_user(uid:str, db:Session=Depends(connect_db)):
    data = get_user(uid, db)
    return await data
    
@router.post('/register', 
    status_code=status.HTTP_201_CREATED,
    # response_model=ShowUser,
    response_model_exclude=['upw'])
async def create_user(request:User, db:Session=Depends(connect_db)) -> ShowUser:
    return await crud.create_user(request, db)

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends(),
                db: Session=Depends(connect_db)):
    user = await validate_user(request,db)
    
    if not user:
      raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
      )
    
    access_token = create_access_token(data={"sub":user.uid})
    token = jsonable_encoder(access_token)
    content = {"message": f"You've successfully logged in. Welcome back, {user.uid}!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite='Lax',
        secure=False,
    )
    return response

@router.get("/users/whoami", dependencies=[Depends(get_current_user)],
            response_model=User,
            response_model_include=['uid'])
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.delete(
    "/user/{uid}",
    response_model=Status,
    # responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_user(
    uid: str, current_user: Status = Depends(get_current_user),
    db: Session=Depends(connect_db)
) -> Status:
    return await crud.delete_user(uid, current_user, db)