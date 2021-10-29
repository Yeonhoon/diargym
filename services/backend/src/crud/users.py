from fastapi import HTTPException, APIRouter,status, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import null
from starlette.status import HTTP_302_FOUND, HTTP_404_NOT_FOUND
from passlib.context import CryptContext
from src.schemas.users import User, ShowUser
from src.schemas.token import Status
from src.database.models import Users, get_db
import psycopg2 as pg

router = APIRouter(
    tags=['users']
)
# conn = pg.connect(
#     dbname='postgres', 
#     user='postgres', 
#     password='postgres', 
#     port='5432')
# cursor = conn.cursor()

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
connect_db = get_db


def produce_hash_password(password: str):
    return pwd_cxt.hash(password)


async def create_user(request, db):
    try:
        new_user = Users(
                uid=request.uid,
                uname= request.uname, 
                uemail = request.uemail,
                upw= produce_hash_password(request.upw))
    except:
        raise HTTPException(
            status_code=HTTP_302_FOUND,
            detail="이미 가입되어있는 아이디입니다."
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "sign up success"
    # response = RedirectResponse(url='/home')

async def check_user(uid:str, db):
    userid = db.query(Users).filter(Users.uid == uid).first()
    # print(userid.uid)
    if userid:
        response:int=0

    else:
        response:int=1

    return response

async def delete_user(uid:str, current_user, db) -> Status:
    db_user = db.query(Users).filter(Users.uid == uid).first()
    
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User '{uid}' not found")

    if db_user.uid == current_user.uid:
        deleted_count = db.query(Users).filter(Users.uid==uid).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"User {uid} not found")
        return Status(message=f"Deleted user {uid}")  # UPDATED
        # db_user.delete(synchronize_session=False)
        # db.commit()
    # return f"User '{current_user}' deleted"

