# 3-1 ベースとなるイメージの指定
FROM mysql:5.7

EXPOSE 3306

# 3-2 コンテナの設定を記述
# 文字コードの設定のセット
COPY mysql.cnf /etc/mysql/conf.d/mysql.cnf
# 初期化用のSQLファイルのセット
COPY init.sql /docker-entrypoint-initdb.d/init.sql