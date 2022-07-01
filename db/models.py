from sqlalchemy import  Column,  String, Integer
from .database import Base

class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key = True,autoincrement=True)
    value =  Column(String, unique = True, nullable = False )
