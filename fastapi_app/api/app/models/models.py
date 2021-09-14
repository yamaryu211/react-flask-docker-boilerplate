# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from .. import db

# userテーブルのモデルUserTableを定義
# 社員情報データベース
class User(db.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

# 顧客情報データベース
class Client(db.Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    company = Column(Boolean(), default=False, nullable=False)
    email = Column(String(64), nullable=False, unique=True) # uniqueである必要あり
    address = Column(String(128), nullable=False)

    projects = relationship('Project',back_populates='client')

# 案件データベース
class Project(db.Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(64), nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))

    # Relationship
    client = relationship('Client',back_populates='projects')


# テーブルが存在しなければ、テーブルを作成
db.Base.metadata.create_all(bind=db.ENGINE)