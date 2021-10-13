from fastapi import APIRouter,Depends, Response, Request, Form
from fastapi.responses import HTMLResponse
from src.database.models import get_db
from sqlalchemy.orm import Session
from src.crud.records import get_all_records, add_record
from src.schemas.records import Record, ShowRecord, RecordBase
from typing import List
from src.schemas.users import ShowUser
from src.auth.jwthandler import get_current_user
router = APIRouter(
    tags=['records']
)

connect_db = get_db

# @router.post('/uploadfile')
# async def create_upload_file(files: List[UploadFile]=File(...)):
#     return {'filenames': [file.filename for file in files]}
@router.get('/getrecords', dependencies=[Depends(get_current_user)],
            response_model=List[ShowRecord],
            response_model_exclude=['rid','ruserid'])
async def get_records(current_user: ShowUser=Depends(get_current_user), db: Session=Depends(connect_db)):
    data = get_all_records(current_user,db)
    return await data

@router.post('/adddiary') 
async def add_records(request: RecordBase, 
                    current_user:ShowUser=Depends(get_current_user),
                    db: Session=Depends(connect_db)  
                    ):
    return await add_record(request, current_user, db)
