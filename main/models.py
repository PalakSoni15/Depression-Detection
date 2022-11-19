from pydantic import BaseModel
from typing import Optional, Union
from fastapi import Form

class User(BaseModel):
    name: str
    email: str
    dob: str
    gender: str
    password: str

class Questionaier(BaseModel):
    que1: Optional[str] = Form()
    # que2: Optional[str]
    # que3: Optional[str]
    # que4: Optional[str]

