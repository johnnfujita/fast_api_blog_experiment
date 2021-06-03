
from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas,database, models
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..JWT import create_access_token

router = APIRouter(
    tags=["Authentication"]
)

### send more fields, send less fields, change types of fields, send empty fields, send imense fields, send invalid json
@router.post("/login", response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models._User).filter(models._User.email == request.username).first()
    if not user:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.password):  
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    access_token = create_access_token(
        data = {"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}