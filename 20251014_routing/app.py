from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!DOCTYPE html>
    <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <title>20251014_routing</title>
        </head>
        <body>
            <h1>index</h1>
        </body>
    </html>
    '''
    return html

# routeでURLをきめる
@app.route('/hello')
# ※先頭の/は必須(ルート)
# このURLに対応する処理を
# 関数で定義する。
# 関数名はなんでもOK。(URLと不一致でもOK)
# ただし、ダブりはないこと。
def hello():
    return 'hello'

# @app.route('/hello2')
# def hello():
#     return 'hello2'
# ダブりは起動しない


# エンドポイント
# URLに紐づいた処理をエンドポイントと言う。
# 既定では関数名がエンドポイント名となる。
# 主に後述のurl_forにて利用する。
# また、app.routeで指定したURLのことをルール(rule)と言う。
# flask routes コマンドで確認可能
# ※app.pyが存在するディレクトリにて実行すること。

# エンドポイント名の変更
@app.route('/a', endpoint='b')
def a():
    return 'a'

@app.route('/a2', endpoint='b2')
def a():
    return 'a2'

# endpointは、関数名のダブり他、関数名が長い場合や、
# 関数の命名規則とURLの命名規則を変えたい場合に用いる。

# データ受け取りのrule
# routeにて、<変数名>とする。
@app.route('/c/<id>')
def c(id):
    return id
# 引数名は、ruleに指定した変数名と同一にする必要がある

# 複数のデータも受け取れる
@app.route('/c/<id>/<name>')    # 上記と同じcだけど、id/nameで区別が付くのでOK
def d(id, name):                # でもこっちはcじゃダメ。関数名の重複はNG(エンドポイント指定で回避可)
    return id + name

# コンバーター
#  受け取るデータの型を定義することができる。
@app.route('/e/<int:id>')
def e(id):
    return str(id + 1)
    # 戻り値はstrである必要がある

    # 型が違うとNot Foundになる。

#[型一覧]
# string:スラッシュなしのテキスト
# int:正の整数
# float:正の浮動小数点
# path:スラッシュ付きのテキスト
# uuid:UUID

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)