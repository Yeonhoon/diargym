from fastapi import HTTPException, APIRouter, status, Depends
from src.database.models import Records, get_db
from src.schemas.records import Record
from sqlalchemy.orm import Session
import psycopg2 as pg


connect_db = get_db
conn = pg.connect(dbname="postgres", user="postgres",password="postgres")

async def get_all_records(current_user, db):
    return await db.query(Records).filter(Records.ruserid==current_user.uid).all()

async def add_record(request, current_user, db):
    w=request.rweight.rstrip()
    u=request.runit.rstrip()
    r=request.rrep.rstrip()
    
    weightlist= w.rsplit(' ')
    unitlist = u.rsplit(' ')
    replist = r.rsplit(' ')
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
    
    return  await "기록이 완료되었습니다."

    # x= {c.name: getattr(data, c.name) for c in data.__table__.columns}
    # print(x['runit'])

    



    