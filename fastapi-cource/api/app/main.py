from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware  # CORSを回避するために必要
from .src import  models
from .src.database import ENGINE
from .src.routers import blog, user, authentication

app = FastAPI()

# CORSを回避するために設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
