from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Optional
from .schemas import TokenData


SECRET_KEY = "a8a998a87f979e97a9d798a89f9a87a98f9a897f9a87f9a98f7a98"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + timedelta(expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data