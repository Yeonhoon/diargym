from sqlalchemy.orm import Session, relation, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import Date

DATABASE_URL = 'postgresql://postgres:postgres@db:5432/postgres'

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

    records = relationship('Records', back_populates='users')

class Workout(Base):
    __tablename__ ='workout'
    wname = Column(String(length=100), primary_key=True, index=True)
    wcategory = Column(String, nullable=False)
    wtype = Column(String)

    records = relationship('Records', back_populates='workout')

class Records(Base):
    __tablename__ = 'records'
    rid = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    ruserid = Column(String(length=20), ForeignKey('users.uid'))
    rdate = Column(String)
    # rlarge = Column(String(length=100), nullable=True)
    # rmid = Column(String(length=100), nullable=True)
    rsmall = Column(String(length=100), ForeignKey('workout.wname'))
    rweight = Column(Float, nullable=False)
    runit = Column(String, nullable=False)
    rrep = Column(Integer, nullable=False)

    users = relationship('Users', back_populates='records')
    workout = relationship('Workout', back_populates='records')

    

  
  
  