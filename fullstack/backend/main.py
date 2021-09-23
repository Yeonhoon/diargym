from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from sql import models,database

import psycopg2 as pg
app = FastAPI()

conn = pg.connect(
    dbname='postgres', 
    user='postgres', 
    password='Zpflrjs94!', 
    port='5432')

connect_db = database.get_db

@app.get('/')
def get_all(db:Session=Depends(connect_db)):
    blogs = db.query(models.Blog).all()
    return blogs

    