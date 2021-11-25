from fastapi import HTTPException, APIRouter, status, Depends, Response
from numpy import pi
from sqlalchemy.sql.expression import true
from starlette.status import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from src.database.models import Records, get_db, Workout
from src.schemas.records import Record, ShowRecord
from sqlalchemy.orm import Session
import psycopg2 as pg
import pandas as pd

connect_db = get_db

# 운동 리스트 불러오기
async def load_wokrout_list(db):
    rawData = db.query(Workout).all()
    # print(rawData)

    return rawData
    # df = pd.read_sql(rawData.statement, rawData.session.bind)
    # print(df)

# 운동 세트정보: 과거운동기록 불러오기 위해
async def get_set_records(current_user,db):
    rawData = db.query(Records,Workout)\
                .join(Workout, Workout.wname == Records.rsmall)\
                .filter(Records.ruserid==current_user.uid)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    df['rdate'] = pd.to_datetime(df['rdate'],format='%Y-%m-%d')
    temp = pd.to_datetime(df['rdate'], ).dt.date
    filtered_date=sorted(list(set(temp)))[-7:] # 최근 7일 데이터만 불러오기
    df = df[df['rdate'].dt.date.isin(filtered_date)]
    df['rdate'] = df['rdate'].astype('str')
    if len(df)>0:
        json = df.to_json(orient="records")
        return Response(content=json, media_type='application/json')
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

async def get_all_records(current_user, db):
    rawData = db.query(Records,Workout)\
                .join(Workout, Workout.wname == Records.rsmall)\
                .filter(Records.ruserid==current_user.uid)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    if(len(df)>0):
        dataset=df.groupby(['rdate','wcategory','rsmall']).sum().reset_index()
        dataset['volume']=dataset['rweight']*dataset['rrep']
        dataset['rdate'] = pd.to_datetime(dataset['rdate'],format='%Y-%m-%d')
        temp = pd.to_datetime(dataset['rdate'], ).dt.date
        filtered_date=sorted(list(set(temp)))[-7:] # 최근 7일 데이터만 불러오기
        dataset = dataset[dataset['rdate'].dt.date.isin(filtered_date)]
        dataset['rdate'] = dataset['rdate'].astype('str')
        # print(dataset)
        pivoted= dataset.pivot_table(index='rdate',columns=['wcategory','rsmall'],values=['rweight','rrep','volume'],fill_value=0).reset_index()
        melted = pivoted.melt(
                        id_vars=['rdate'],
                        # value_vars=pivoted.columns[1:].tolist(),
                        # var_name = "category",
                        # value_name="volume"
                        )
        # print(melted)
        melted.rename(columns={None:'type','rsmall':'category'}, inplace=True)
        json = melted.to_json(orient="records")
        return Response(content=json, media_type='application/json')
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

async def get_tables_record(current_user,db):
    rawData = db.query(Records,Workout)\
                .join(Workout, Workout.wname == Records.rsmall)\
                .filter(Records.ruserid==current_user.uid)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    df['rdate'] = df['rdate'].astype('str')
    df=df.sort_values(by="rdate",ascending=False)
    print(df)
    json = df.to_json(orient="records")
    return Response(content=json, media_type='application/json')

async def get_tables_record_date(current_user,db, rdate):
    rawData = db.query(Records,Workout)\
                .join(Workout, Workout.wname == Records.rsmall)\
                .filter(Records.ruserid==current_user.uid)\
                .filter(Records.rdate == rdate)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    df['rdate'] = df['rdate'].astype('str')
    json = df.to_json(orient="records")
    return Response(content=json, media_type='application/json')

async def dashbar_records(category, current_user, db):
    rawData = db.query(Records,Workout)\
                .join(Workout, Workout.wname == Records.rsmall)\
                .filter(Records.ruserid==current_user.uid)
    df = pd.read_sql(rawData.statement, rawData.session.bind)
    df= df[df['wcategory']==category]
    df['rdate'] = df['rdate'].astype('str')
    df['volume']=df['rweight']*df['rrep']
    # print(df)
    pivoted= df.pivot_table(index='rdate',columns=['wcategory','rsmall'],values=['volume'],fill_value=0, aggfunc='sum').reset_index()
    print(pivoted)
    melted = pivoted.melt(id_vars=['rdate'])
    melted.rename(columns={None:'type'}, inplace=True)
    melted.sort_values(['rsmall','rdate'], inplace=True)
    # print(melted)
    # print(melted.groupby(['rdate','rmid'])['value'].mean())
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


async def update(rid:int, request, current_user, db):
    try:
        record = db.query(Records).filter(Records.rid == rid)
    except:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            datail= "존재하지 않는 기록입니다."
        )
    if record.first().ruserid == current_user.uid:
        record.update({
            Records.ruserid : current_user.uid,
            Records.rdate : request.rdate,
            Records.rweight : request.rweight,
            # Records.rlarge : request.rlarge,
            # Records.rmid : request.rmid,
            Records.rsmall : request.rsmall,
            Records.rrep : request.rrep,
            Records.runit : request.runit,
        })
        db.commit()
        return Response(status_code=HTTP_202_ACCEPTED)
    
async def delete(rid: int, current_user, db):
    try:
        record = db.query(Records).filter(Records.rid == rid).first()
        print(record)
    except:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND,
          detail=f"Record {rid} not found"
        )
    # ruserid가 없나?
    if record.ruserid == current_user.uid:
        db.delete(record)
        db.commit()

    return Response(status_code=HTTP_204_NO_CONTENT)
    



    