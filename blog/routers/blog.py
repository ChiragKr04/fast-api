from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = database.get_db


# Getting all blogs
@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(db)


# Creating New Blog
@router.post('/', status_code=status.HTTP_200_OK, response_model=schemas.Blog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


# Deleting a blog
@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog.delete(blog_id, db)


# Updating a blog
@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(blog_id, request, db)


# Getting blog by ID
@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_single_blog(blog_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_single(blog_id, db)
