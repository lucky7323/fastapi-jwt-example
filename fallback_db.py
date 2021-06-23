from datetime import datetime
from models import User
import bcrypt


pass1 = "qwer1234"
pass2 = "qlalfqjsgh!!"
DB = [
    User(id=0, email="eunho@test.com",
         password=bcrypt.hashpw(pass1.encode("utf-8"), bcrypt.gensalt()).decode(),
         companyJoinDate=datetime(year=2019, month=11, day=15)),
    User(id=1, email="dookyung@test.com",
         password=bcrypt.hashpw(pass2.encode("utf-8"), bcrypt.gensalt()).decode(),
         companyJoinDate=datetime(year=2021, month=6, day=21)),
]


