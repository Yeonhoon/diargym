# from sqlalchemy.orm.session import Session
# from blog.router import authentication
# from psycopg2 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# POSTGRES_DATABASE_URL = 'postgresql://postgres:Zpflrjs94!@postgres:5432/postgres'
# pgEngine = create_engine(POSTGRES_DATABASE_URL, connect_args={'check_same_thread':False})

# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=pgEngine))

# def get_pgDb():
#   db = SessionLocal()
#   try:
#     yield db
#   finally:
#     db.close()