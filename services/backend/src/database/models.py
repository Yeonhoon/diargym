from sqlalchemy.orm import Session, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = 'postgresql://postgres:postgres@172.19.0.2:5432/postgres'

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
  uid = Column(String(length=20), primary_key = True, index =True)
  uname = Column(String, nullable=False)
  uemail = Column(String, nullable=False)
  upw = Column(String, nullable=False)

  posts = relationship('Posts', back_populates='users')


class Posts(Base):
  __tablename__ = 'posts'
  pid = Column(Integer, primary_key=True, index=True)
  ptitle = Column(String, nullable=False)
  pcontent = Column(String,nullable=False)
  author = Column(String(length=20), ForeignKey('users.uid'))
  
  users = relationship('Users', back_populates='posts')