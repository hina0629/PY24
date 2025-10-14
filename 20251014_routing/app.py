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

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)