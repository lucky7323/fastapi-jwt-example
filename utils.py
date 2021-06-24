import sqlite3
import pandas as pd
from models import User


def is_user_exist(email: str):
    conn = sqlite3.connect("database/dayoff.db")
    df = pd.read_sql_query("SELECT * FROM tb_user", conn)
    conn.close()

    df = df[df['email'] == email]
    if df.empty:
        return False
    else:
        return True


def find_by_id(user_id: int):
    conn = sqlite3.connect("database/dayoff.db")
    df = pd.read_sql_query("SELECT * FROM tb_user", conn)
    conn.close()

    df = df[df['user_id'] == user_id]
    if df.empty:
        return None
    if len(df) == 1:
        return User(**dict(df.loc[0]))
    else:
        return None

