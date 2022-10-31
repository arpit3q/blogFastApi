from sys import prefix
from fastapi import APIRouter, Depends
from schemas import User, ShowUser
from sqlalchemy.orm import Session
from database import get_db
from repository import user

router = APIRouter(
    prefix= "/user",
    tags= ["Users"]
)

@router.post('/', response_model= ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', response_model= ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.get_user(id, db)
