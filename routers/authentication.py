from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas import Login
from sqlalchemy.orm import Session
from models import User
from hashing import Hash
from JWTtoken import create_access_token

router = APIRouter(
    tags = ["Login"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail="Invalid password")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}