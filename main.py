import bcrypt
import utils
import sqlite3
import pandas as pd
from datetime import datetime
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from models import User
from auth import create_token, get_current_user


app = FastAPI()


@app.post("/api/login")
def login(user_info: User):
    is_exist = utils.is_user_exist(user_info.email)

    if not is_exist:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

    conn = sqlite3.connect("database/dayoff.db")
    df = pd.read_sql_query("SELECT * FROM tb_user", conn)
    conn.close()

    df = df[df['email'] == user_info.email]
    if df.empty or len(df) != 1:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_USER"))

    is_verified = bcrypt.checkpw(user_info.password.encode("utf-8"),
                                 df.loc[0]['password'].encode("utf-8"))
    if not is_verified:
        return JSONResponse(status_code=400, content=dict(msg="NO_MATCH_PASSWORD"))
    token = {
        "Authorization":
        f"Bearer {create_token(User(**dict(df.loc[0])))}"
    }
    return token


@app.get("/api/users")
def get_users(user: User = Depends(get_current_user)):
    return user


"""
@app.put("/api/users")
async def put_users(user: User = Depends(get_current_user)):
    for db_user in fallback_db.DB:
        db_user.
"""


