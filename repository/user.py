from sqlalchemy.orm import Session
from models import User as U
from hashing import Hash
from schemas import User
from fastapi import HTTPException, status

def create(request: User, db: Session):
    new_user = U(name=request.name, email= request.email, password= Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session):
    user = db.query(U).filter(U.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail=f"User with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Blog with the id {id} is not available"}
    return user