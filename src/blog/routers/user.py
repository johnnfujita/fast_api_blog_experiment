
from fastapi import APIRouter, HTTPException, Depends, status, Response
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
router = APIRouter(
    prefix="/user",
    tags=["users"]
)






@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=schemas._UserShow)
def create_user(_user: schemas._User, db: Session = Depends(database.get_db)):
    hashed_password = Hash.hash_password(_user.password)
    new_user = models._User(name=_user.name, email=_user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", status_code=200, response_model=schemas._UserShow)
def get_user_by_id(id:int, db: Session =Depends(database.get_db)):
    user = db.query(models._User).filter(models._User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with the id {id} not found")
    return user