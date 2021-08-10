from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, HTTPException


def get(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, is_published=request.is_published, user_id=2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Id {blog_id} not found"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return {
        "status_code": status.HTTP_204_NO_CONTENT,
        "detail": f"Blog with Id {blog_id} successfully deleted"
    }


def update(blog_id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Id {blog_id} not found"
        )
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return {
        "status_code": status.HTTP_202_ACCEPTED,
        "detail": f"Blog with Id {blog_id} successfully updated"
    }


def get_single(blog_id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Id {blog_id} not found"
        )
    return blog
