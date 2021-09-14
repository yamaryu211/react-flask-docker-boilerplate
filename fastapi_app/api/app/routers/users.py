from fastapi import APIRouter
from typing import List  # ネストされたBodyを定義するために必要
from .. import db  # DBと接続するためのセッション
from ..models import models  # 今回使うモデルをインポート
from ..schemas import users as user_schema # 上記各モデルに対応したスキーマをインポート

router = APIRouter()

# ----------APIの実装------------
# テーブルにいる全ユーザ情報を取得 GET
@router.get("/users")
def read_users():
    users = db.session.query(models.User).all()
    return users

# idにマッチするユーザ情報を取得 GET
@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = db.session.query(models.User).\
        filter(models.User.id == user_id).first()
    return user

# ユーザ情報を登録 POST
@router.post("/user")
# クエリでnameとstrを受け取る
# /user?name="三郎"&age=10
async def create_user(name: str, age: int):
    user = models.User()
    user.name = name
    user.age = age
    db.session.add(user)
    db.session.commit()

# 複数のユーザ情報を更新 PUT
@router.put("/users")
# modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[user_schema.User]):
    for new_user in users:
        user = db.session.query(models.User).\
            filter(models.User.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        db.session.commit()