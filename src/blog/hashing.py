
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    ### tests pending hash null, hash big, hash, bool, hash space
    def hash_password(password: str):
        return pwd_cxt.hash(password)
    ## send one only, send none, send large string, send not string
    def verify( plain_password, hashed_password):
        return pwd_cxt.verify(plain_password, hashed_password)   