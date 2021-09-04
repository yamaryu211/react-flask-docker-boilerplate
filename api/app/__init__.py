from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR # MySQLのテーブル作成の際に必要

app = Flask(__name__)

app.config.from_object('app.config.Config') # config.pyの設定内容を読み込み

# dbの初期化
db = SQLAlchemy(app)
Migrate(app,db)

# models.py
from app import models #順番に注意。でないと循環参照となりエラー。
app.register_blueprint(models.models_blueprint)

@app.route('/api/v1.0/test', methods=['GET'])
def test_response():
    """Return a sample JSON response."""
    sample_response = {
        "items": [
            { "id": 1, "name": "Apples",  "price": "$2" },
            { "id": 2, "name": "Peaches", "price": "$5" }
        ]
    }
    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    # Mozilla provides good references for Access Control at:
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control

    return response

#if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=5000,debug=True)