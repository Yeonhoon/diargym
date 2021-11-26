from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import users, records

app=FastAPI()

origins = [
    "http://118.67.132.200:8080",
    "http://localhost:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(records.router)



