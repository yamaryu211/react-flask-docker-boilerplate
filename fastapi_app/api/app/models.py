# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from . import db


# userテーブルのモデルUserTableを定義
class User(db.Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)

def main():
    # テーブルが存在しなければ、テーブルを作成
    db.Base.metadata.create_all(bind=db.ENGINE)


if __name__ == "__main__":
    main()