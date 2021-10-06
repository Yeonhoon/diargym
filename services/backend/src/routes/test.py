from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import HTMLResponse
from typing import List
import pandas as pd
router = APIRouter(
    tags=['test']
)

@router.post('/uploadfile')
async def create_upload_file(files: List[UploadFile]=File(...)):
    return {'filenames': [file.filename for file in files]}