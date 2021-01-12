import secrets
from datetime import datetime, timedelta
import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials, HTTPBearer

auth = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@auth.get("/basic-beginning")
def read_with_basic_beginning(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    return {"username": credentials.username, "password": credentials.password}


basic_security = HTTPBasic()


def basic_authentication(credentials: HTTPBasicCredentials = Depends(basic_security)) -> str:
    correct_username = secrets.compare_digest("jes", credentials.username)  # reduce the risk of timing attacks
    print('token:', secrets.token_urlsafe(16))  # secrets.token_hex(16)
    bd_hashed_password = bcrypt.hashpw(b"pass", bcrypt.gensalt())
    correct_password = bcrypt.checkpw(credentials.password.encode('utf-8'), bd_hashed_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password",
        )
    return credentials.username


@auth.get("/basic")
def read_with_basic(username: str = Depends(basic_authentication)):
    return {"username": username}


@auth.post("/bearer")
def create_jwt_token(username: str = Depends(basic_authentication)):
    expire = datetime.utcnow() + timedelta(minutes=60)
    encoded_jwt = jwt.encode({'sub': username, 'exp': expire}, 'secret_key-Y01oEAl3iz', algorithm='HS256')
    return {"token": encoded_jwt}


bearer_security = HTTPBearer()


def bearer_authentication(credentials: HTTPAuthorizationCredentials = Depends(bearer_security)) -> str:
    try:
        payload = jwt.decode(credentials.credentials, 'secret_key-Y01oEAl3iz', algorithms=["HS512", "HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non username")
        if username not in ["jes"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return username
    except jwt.DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="expired token")


@auth.get("/bearer")
def read_with_jwt_token(username: str = Depends(bearer_authentication)):
    return {"username": username}
