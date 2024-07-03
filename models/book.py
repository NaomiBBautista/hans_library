from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Book(Base):
    __tablename__ = "books"
    
    code = Column(Integer, primary_key=True, autoincrement=True)
    title =  Column(String)
    author = Column(String)
    year = Column(Integer)
    pages = Column(Integer)
    id_category = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship("Category", back_populates="books")