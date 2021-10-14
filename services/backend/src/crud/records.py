from fastapi import HTTPException, APIRouter, status, Depends, Response
from numpy import pi
from src.database.models import Records, get_db
from src.schemas.records import Record
from sqlalchemy.orm import Session
import psycopg2 as pg
import pandas as pd

connect_db = get_db
conn = pg.connect(dbname="postgres", user="postgres",password="postgres")


async def get_all_records(current_user, db):
    rawData = db.query(Records).filter(Records.ruserid==current_user.uid)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    dataset=df.groupby(['rdate','rmid','rsmall']).sum().reset_index()
    dataset['rdate'] = dataset['rdate'].astype('str')
    dataset['volume']=dataset['rweight']*dataset['rrep']
    pivoted= dataset.pivot_table(index='rdate',columns='rmid',values='volume',fill_value=0).reset_index()
    melted = pivoted.melt(
                    id_vars=['rdate'],
                    value_vars=pivoted.columns[1:],
                    var_name = "category",
                    value_name="volume"
                    )
    
    json = melted.to_json(orient="records")
    return Response(content=json, media_type='application/json')


async def add_record(request, current_user, db):
    w = request.rweight.rstrip()
    u = request.runit.rstrip()
    r = request.rrep.rstrip()
    
    weightlist= w.split(' ')
    unitlist = u.split(' ')
    replist = r.split(' ')

    for i in range(len(weightlist)):
        data = Records(ruserid = current_user.uid,
                  rdate= request.rdate,
                  rlarge = request.rlarge,
                  rmid = request.rmid,
                  rsmall = request.rsmall,
                  rweight = weightlist[i],
                  runit = unitlist[i],
                  rrep = replist[i]
                  )
    
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="추가할 수 없음.")

        db.add(data)
        db.commit()
        db.refresh(data)
    
    return  "기록이 완료되었습니다."

    # x= {c.name: getattr(data, c.name) for c in data.__table__.columns}
    # print(x['runit'])

    



    