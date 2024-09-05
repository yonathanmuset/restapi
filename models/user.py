from sqlalchemy import Column, String, Integer
from config.db import meta, engine, Base

meta.create_all(engine)


class user(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
