from sys import prefix
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from schemas import *
from database import get_db
from models import Blog as B
from sqlalchemy.orm import Session
from repository import blog
from oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags =["Blogs"]
)


@router.get('/', response_model=List[ShowBlog])
def all(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.create(request, db)

@router.put('/{id}', status_code=202)
def update(id: int, request: Blog, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=204)
def destroy(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.destroy(id, db)

@router.get('/{id}', status_code=200, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return blog.show(id, db)
