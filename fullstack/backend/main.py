from fastapi import FastAPI, status, Depends

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse, Response
from .router import user, authentication


app = FastAPI( )
app.include_router(user.router)
app.include_router(authentication.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://172.23.43.172:8080", 'http://localhost:8080'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

