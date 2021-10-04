from sqlalchemy.orm import Session, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = 'postgresql://postgres:Zpflrjs94!@127.0.0.1:5432/postgres'

engine = create_engine(DATABASE_URL)

db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))
Base = declarative_base()

def get_db():
  db = db_session()
  try:
    yield db
  finally:
    db.close()

class Users(Base):
  __tablename__ = 'users'
  uid = Column(Integer, primary_key= True, index =True)
  uname = Column(String)
  uemail = Column(String)
  upw = Column(String)

  posts = relationship('Posts', back_populates='users')


class Posts(Base):
  __tablename__ = 'posts'
  pid = Column(Integer, primary_key=True, index=True)
  ptitle = Column(String)
  pcontent = Column(String)
  author = Column(Integer, ForeignKey('users.uid'))
  
  users = relationship('Users', back_populates='posts')