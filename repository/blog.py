from sqlalchemy.orm import Session
from models import Blog as B
from fastapi import HTTPException, status
from schemas import Blog

def get_all(db: Session):
    blogs = db.query(B).all()
    return blogs

def create(request: Blog, db: Session):
    new_blog = B(title=request.title, body= request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(B).filter(B.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail= f"blog with the id {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id: int, request: Blog, db: Session):
    blog = db.query(B).filter(B.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail= f"blog with the id {id} is not found")
    blog.update(request.dict())
    db.commit()
    return "updated"

def show(id: int, db: Session):
    blog = db.query(B).filter(B.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                detail=f"Blog with the id {id} is not available")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f"Blog with the id {id} is not available"}
    return blog