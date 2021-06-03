from fastapi import APIRouter, HTTPException, Depends, status, Response
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
    
)

@router.post("/", status_code=status.HTTP_201_CREATED)
# YOU CAN DEFINE WHAT ATTRIBUTES WILL BE RETURNED IN THE RESPONSE when you define response_model and choose a pydantic schema
def create_post(blog: schemas.ShowBlog, db: Session = Depends(database.get_db)):
    
    new_blog = models.Blog(title=blog.title, body=blog.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete("/{id}", status_code=200 )
def destroy(id, db: Session = Depends(database.get_db)):
    queried_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not queried_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
    queried_blog.delete(synchronize_session=False)
    db.commit()
    return {"blog": id, "status": "deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: schemas.Blog, db: Session = Depends(database.get_db)):
    queried_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not queried_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
    queried_blog.update(blog)
    db.commit()
    return {"Status": "Update Successfull"}


@router.get("/", response_model=List[schemas.Blog])
def all_blog(db: Session = Depends(database.get_db), current_user: schemas._UserShow = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/{id}", status_code=200,  response_model=schemas.Blog)
def get_blog(id, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Item {id} is not available"}
    return blog