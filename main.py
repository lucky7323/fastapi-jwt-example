import bcrypt
import utils
import fallback_db
from datetime import datetime
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from models import User
from auth import create_token, get_current_user


app = FastAPI()


@app.post("/api/login")
async def login(user_info: User):
    is_exist = await utils.is_user_exist(user_info.email)
    # TODO: user_info validations

    if not is_exist:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

    # TODO: DB 조회
    for user in fallback_db.DB:
        if user.email == user_info.email:
            a = user_info.password.encode("utf-8")
            b = user.password.encode("utf-8")
            is_verified = bcrypt.checkpw(user_info.password.encode("utf-8"),
                                         user.password.encode("utf-8"))
            if not is_verified:
                return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_PASSWORD"))
            token = {
                "Authorization":
                f"Bearer {create_token(user)}"
            }
            return token
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))


@app.get("/api/users")
async def get_users(admin: User = Depends(get_current_user)):
    return admin



