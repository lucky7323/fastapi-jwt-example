from datetime import datetime
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    user_id: int
    email: EmailStr
    password: str
    company_join_date: datetime



