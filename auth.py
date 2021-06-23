import jwt
import utils
from fastapi import HTTPException
from datetime import datetime
from typing import Optional
from datetime import timedelta
from models import User


# TODO: secure secret key & algorithms
SECRET = "mysecret"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(payload=to_encode, key=SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def create_token(user: User):
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"user_id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


async def get_current_user(token: str):
    credentials_exception = HTTPException(status_code=400)
    try:
        payload = jwt.decode(token, SECRET, algorithms=ALGORITHM)
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception

    except jwt.exceptions.InvalidTokenError:
        raise credentials_exception
    user = await utils.find_by_id(user_id)
    if user is None:
        raise credentials_exception
    return user

