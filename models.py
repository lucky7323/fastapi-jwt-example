from datetime import datetime
from pydantic.main import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    companyJoinDate: datetime



