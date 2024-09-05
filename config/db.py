from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///sql_app.db", echo=True)
meta = MetaData()
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session
conm = engine.connect()
