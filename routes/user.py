from fastapi import APIRouter, Response
from sqlalchemy import select, delete, update
from config.db import conm
from models.user import user as User
from schemas.user import usuario
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()


@user.get("/users", response_model=list[usuario], tags=["user"])
def get_users():
    result = conm.execute(select(User)).fetchall()
    users = [dict(row._mapping) for row in result]
    return users


@user.post("/users", response_model=list[usuario], tags=["user"])
def create_user(user: usuario):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conm.execute(User.__table__.insert().values(new_user))
    conm.commit()
    last_inserted_id = result.lastrowid
    inserted_user = conm.execute(
        select(User).where(User.id == last_inserted_id)
    ).first()
    inserted_user_dict = dict(inserted_user._asdict())
    return inserted_user_dict


@user.get("/users/{id}", response_model=list[usuario], tags=["user"])
def get_user(id: str):
    result = conm.execute(select(User).where(User.id == id)).first()
    user_result = result._asdict()
    return user_result


@user.delete("/users/{id}", response_model=list[usuario], tags=["user"])
def delete_user(id: str):
    result = conm.execute(delete(User).where(User.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model=list[usuario], tags=["user"])
def update_user(id: str, user: usuario):
    conm.execute(
        update(User)
        .values(
            name=user.name,
            email=user.email,
            password=f.encrypt(user.password.encode("utf-8")),
        )
        .where(User.id == id)
    )
    result = conm.execute(select(User).where(User.id == id)).first()
    result_dict = result._asdict()
    return result_dict
