import asyncio
import fallback_db


async def is_user_exist(email: str):
    # TODO: DB 조회
    await asyncio.sleep(3)
    for user in fallback_db.DB:
        if email == user.email:
            return True
    return False


async def find_by_id(user_id: int):
    # TODO: DB 조회
    await asyncio.sleep(3)
    for user in fallback_db.DB:
        if user_id == user.id:
            return user
    return None

