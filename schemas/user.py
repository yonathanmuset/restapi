from typing import Optional
from pydantic import BaseModel


class usuario(BaseModel):

    id: Optional[str]
    name: str
    email: str
    password: str


class Config:
    orm_mode = True
