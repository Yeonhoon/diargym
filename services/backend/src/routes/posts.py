from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud import posts as crud
from src.auth.jwthandler import get_current_user
from src.schemas.posts import ShowPost, Post
from src.schemas.token import Status
from src.schemas.users import ShowUser


router = APIRouter(
  tags=['posts']
)


@router.get(
    "/posts",
    response_model=List[ShowPost],
    dependencies=[Depends(get_current_user)],
)
async def get_posts():
    return await crud.get_posts()


@router.get(
    "/post/{post_id}",
    response_model=ShowPost,
    dependencies=[Depends(get_current_user)],
)
async def get_post(post_id: int) -> ShowPost:
    try:
        return await crud.get_post(post_id)
    except:
        raise HTTPException(
            status_code=404,
            detail="post does not exist",
        )


@router.post(
    "/posts", response_model=ShowPost, dependencies=[Depends(get_current_user)]
)
async def create_post(
    request: Post, 
    current_user: ShowUser = Depends(get_current_user)
) -> ShowPost:
    return await crud.create_post(request, current_user)


@router.patch(
    "/post/{post_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ShowPost,
    # responses={404: {"model": HTTPException(status_code=status.HTTP_404_NOT_FOUND )}},
)
async def update_post(
    post_id: int,
    request: ShowPost,
    current_user: ShowUser = Depends(get_current_user),
) -> ShowPost:
    return await crud.update_post(post_id, request, current_user)


@router.delete(
    "/post/{post_id}",
    response_model=Status,
    # responses={404: {"model": HTTPException(status_code=status.HTTP_404_NOT_FOUND )}},
    dependencies=[Depends(get_current_user)],
)
async def delete_post(
    post_id: int, current_user: Session = Depends(get_current_user)
):
    return await crud.delete_post(post_id, current_user)