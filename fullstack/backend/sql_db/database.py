
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