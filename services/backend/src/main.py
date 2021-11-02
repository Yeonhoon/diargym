from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn
from src.routes import users,posts, records
# def create_app():
#     c = conf()
#     app = FastAPI()
#     conf_dict = asdict(c)
#     db.init_app(app,)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://118.67.132.200:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(records.router)
@app.get('/')
def home():
    return "Hello FastAPI!"


