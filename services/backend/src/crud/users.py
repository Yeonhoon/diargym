from fastapi import HTTPException, APIRouter,status, Depends, Response
from sqlalchemy.orm import Session
from starlette.status import HTTP_302_FOUND, HTTP_404_NOT_FOUND
from passlib.context import CryptContext
from src.schemas.users import User, ShowUser
from src.schemas.token import Status
from src.database.models import Users, get_db
import psycopg2 as pg

router = APIRouter(
    tags=['users']
)
conn = pg.connect(
    dbname='postgres', 
    user='postgres', 
    password='postgres', 
    port='5432')
cursor = conn.cursor()

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
connect_db = get_db


def produce_hash_password(password: str):
    return pwd_cxt.hash(password)


async def create_user(request, db):
    # sql = "insert into users (uname, uemail, upw) values(%s, %s, %s)"
    # cursor.execute(sql, (request.name, request.email, 
                        # produce_hash_password(request.password)))
    # print(data)
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

# @router.delete('/delteuser', status_code=status.HTTP_200_OK)
async def delete_user(uname:str, current_user, db) -> Status:
    db_user = db.query(Users).filter(Users.uname == uname).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User '{uname}' not found")

    if db_user.uname == current_user.uname:
        deleted_count = db.query(Users).filter(Users.uname==uname).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"User {uname} not found")
        return Status(message=f"Deleted user {uname}")  # UPDATED
        # db_user.delete(synchronize_session=False)
        # db.commit()
    # return f"User '{current_user}' deleted"

