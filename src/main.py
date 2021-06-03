
from fastapi import FastAPI
from .blog.database import engine
from .blog import models


from  .blog.routers import authentication, blog, user

app = FastAPI()



models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

# the session was actually created in the database.py file by the sessionmaker
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"])
# # YOU CAN DEFINE WHAT ATTRIBUTES WILL BE RETURNED IN THE RESPONSE when you define response_model and choose a pydantic schema
# def create_post(blog: schemas.ShowBlog, db: Session = Depends(get_db)):
    
#     new_blog = models.Blog(title=blog.title, body=blog.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete("/blog/{id}", status_code=200, tags=["blogs"])
# def destroy(id, db: Session = Depends(get_db)):
#     queried_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not queried_blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
#     queried_blog.delete(synchronize_session=False)
#     db.commit()
#     return {"blog": id, "status": "deleted"}


# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
# def update_blog(id, blog: schemas.Blog, db: Session = Depends(get_db)):
#     queried_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not queried_blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
#     queried_blog.update(blog)
#     db.commit()
#     return {"Status": "Update Successfull"}


# @app.get("/blog", response_model=schemas.Blog)
# def all_blog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}", status_code=200,  response_model=schemas.Blog)
# def get_blog(id, response: Response, db: Session = Depends(get_db), tags=["blogs"]):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} not found")
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {"detail": f"Item {id} is not available"}
#     return blog


# @app.post("/user", status_code=status.HTTP_201_CREATED,  response_model=schemas._UserShow, tags=["users"])
# def create_user(_user: schemas._User, db: Session = Depends(get_db)):
#     hashed_password = pwd_cxt.hash(_user.password)
#     new_user = models._User(name=_user.name, email=_user.email, password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}", status_code=200, response_model=schemas._UserShow, tags=["users"])
# def get_user_by_id(id:int, db: Session =Depends(get_db)):
#     user = db.query(models._User).filter(models._User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with the id {id} not found")
#     return user


if __name__=="__main__":
    app.run()