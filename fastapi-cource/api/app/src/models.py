from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
from . import database
from pydantic import BaseModel


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64))
    body = Column(String(128))
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30))
    email = Column(String(64))
    password = Column(String(128))

    blogs = relationship('Blog', back_populates="creator")

# テーブルが存在しなければ、テーブルを作成
database.Base.metadata.create_all(bind=database.ENGINE)
