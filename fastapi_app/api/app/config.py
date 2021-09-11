# MySQLの環境変数の設定
import os

class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(**{
        'user': "root",
        'password': "pass",
        'host': "db:3306",
        'database': "sample_db"
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False # おまじない
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig

# DBのhostは、dockerのネットワークを調べたうえで記入する必要あり
# なので、コンテナをbuild,upした後で記入
