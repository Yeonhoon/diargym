from fastapi import APIRouter,Depends, Response, Request, Form
from fastapi.responses import HTMLResponse
from src.database.models import get_db
from sqlalchemy.orm import Session
from src.crud.records import (
    load_wokrout_list,
    get_set_records,
    get_all_records, 
    add_record, 
    get_tables_record, 
    get_tables_record_date,
    dashbar_records,
    update,
    delete
    )
from src.schemas.records import Record, ShowRecord, RecordBase
from typing import List
from src.schemas.users import ShowUser
from src.auth.jwthandler import get_current_user
router = APIRouter(
    tags=['records']
)

connect_db = get_db
@router.get('/workoutlist')
async def workout_list(db:Session=Depends(connect_db)):
    df = load_wokrout_list(db)
    return await df

@router.post('/records') 
async def add_records(request: RecordBase, 
                    current_user:ShowUser=Depends(get_current_user),
                    db: Session=Depends(connect_db)  
                    ):
    return await add_record(request, current_user, db)

@router.get('/records', dependencies=[Depends(get_current_user)],
            response_model=List[ShowRecord],
            response_model_exclude=['ruserid'])
async def get_records(current_user: ShowUser=Depends(get_current_user), db: Session=Depends(connect_db)):
    data = get_set_records(current_user,db)
    return await data

@router.get('/tables', dependencies=[Depends(get_current_user)],
                    response_model=List[ShowRecord],
                    response_model_exclude=['ruserid'])
async def get_tables_records(current_user: ShowUser=Depends(get_current_user), db: Session=Depends(connect_db)):
    data = get_tables_record(current_user, db)
    return await data

@router.get('/tables/{rdate}', dependencies=[Depends(get_current_user)],
                    response_model=List[ShowRecord],
                    response_model_exclude=['rid','ruserid'])
async def get_tables_records(rdate, current_user: ShowUser=Depends(get_current_user), db: Session=Depends(connect_db), 
                            ):
    data = get_tables_record_date(current_user, db, rdate)
    return await data

@router.get('/dashbar/{category}', dependencies=[Depends(get_current_user)],
                    response_model=List[ShowRecord],
                    response_model_exclude=['rid','ruserid'])
async def get_dashbar_records(category, current_user: ShowUser=Depends(get_current_user), 
                            db: Session=Depends(connect_db)):
    data = dashbar_records(category, current_user, db)
    return await data


@router.delete('/delete/{rid}', dependencies=[Depends(get_current_user)])
async def delete_record(rid:int, current_user: ShowUser=Depends(get_current_user), db: Session=Depends(connect_db)):
    print(rid)
    data = delete(rid, current_user, db)
    return await data

@router.patch('/update/{rid}')
async def update_record(rid, 
                    request: ShowRecord,
                    current_user: ShowUser=Depends(get_current_user), 
                    db: Session=Depends(connect_db)):

    data = update(rid, request, current_user, db)
    return await data

