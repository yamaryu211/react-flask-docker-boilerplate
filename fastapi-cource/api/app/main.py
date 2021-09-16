import os
from fastapi import FastAPI
from .src import  models
from .src.database import engine
from .src.routers import blog, user, authentication

basedir = os.path.abspath(os.path.dirname(__file__))

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
