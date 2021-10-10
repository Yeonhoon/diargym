from os import stat
from fastapi import HTTPException, APIRouter, status, Depends
from psycopg2 import connect
from src.database.models import Posts,get_db
from src.schemas.posts import Post, ShowPost
from sqlalchemy.orm import Session

router = APIRouter(
  tags=['posts']
)

connect_db = get_db

async def get_posts(db):
    return await db.query(Posts).all()

async def get_post(pid: int, db: Session=Depends(connect_db)):
    return await db.query(Posts).filter(Posts.pid == pid).all()

# @router.post('/newpost')
async def create_post(request: Post, current_user, db: Session=Depends(connect_db)):
    data = Posts(ptitle= request.ptitle,
                  pcontent=request.pcontent,
                  author = current_user
                  )
    db.add(data)
    db.commit()
    db.refresh(data)
    return "posting success"

async def update_post(pid: int, request, current_user, db):
    try:
        post = db.query(Posts).filter(Posts.pid == pid).first()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post {pid} not found"
            )
    if post['author'] == current_user.uname:
        data = Posts(ptitle = request.ptitle, pcontent = request.pcontent)
        db.update(data)
        db.commit()
        db.refresh(data)
        return await db.query(Posts).filter(Posts.pid == pid).first()

async def delete_post(pid: int, current_user, db):
    try:
        post = db.query(Posts).filter(Posts.pid == pid).first()
    except:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"post {pid} not found"
        )
    if post['author'] == current_user.uname:
        post.delete(synchronize_session=False)
        db.commit()
        return f"User '{pid}' deleted"
