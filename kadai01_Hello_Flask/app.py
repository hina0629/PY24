# pip install flask
# flask
# PythonのWebアプリケーション用
# フレームワーク

# flaskモジュールからFlaskクラスをインポート
from flask import Flask

# Flaskインスタンスの取得
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello flask'

if __name__ == '__main__':
    # Webサーバー起動
    app.run('0.0.0.0', 80, True)