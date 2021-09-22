from fastapi import FastAPI
from . import schemas, models #.: same directory
from .database import engine
from .router import blog, user


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(engine)


