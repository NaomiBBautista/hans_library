from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String)
    password = Column(String)