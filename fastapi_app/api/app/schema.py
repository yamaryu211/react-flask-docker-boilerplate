# スキーマはここで定義
from pydantic import BaseModel

# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int