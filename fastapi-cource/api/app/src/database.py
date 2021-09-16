# -*- coding: utf-8 -*-
# DBへの接続設定
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# テスト用のSQLiteの設定
# SQLALCHAMY_DATABASE_URL = 'sqlite:///app/blog.db'
# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

# 接続したいDBの基本情報を設定
user_name = "docker"
password = "docker"
host = "db"  # docker-composeで定義したMySQLのサービス名
database_name = "sample_db"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DBとの接続
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()