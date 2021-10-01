from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key= True, index =True)
    uname = Column(String)
    uemail = Column(String)
    upw = Column(String)

    blogs = relationship('Blog',back_populates='author')

class Blog(Base):
    __tablename__ = 'blogs'
    bid = Column(Integer, primary_key= True, index =True)
    btitle = Column(String)
    bcontent = Column(String)
    user_id = Column(Integer, ForeignKey('users.uid'))

    author = relationship('User', back_populates="blogs")
    


