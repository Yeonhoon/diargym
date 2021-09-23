from fastapi import FastAPI
from . import schemas, models #.: same directory
from .database import engine
from .router import blog, user, authentication, postgres


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(postgres.router)


models.Base.metadata.create_all(engine)


