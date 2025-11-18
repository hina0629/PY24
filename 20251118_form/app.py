from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 手打ちで127.0.0.1/confirmと打つと見えるけど、
# index.htmlの送信からだと見れない(POSTが許可されていない)
# @app.route('/confirm')
# def confirm():
#     return render_template('confirm.html')

# postを受け取るには、methodsの指定が必要
# 今度は手打ちだと見れなくなる(GETが許可されていない)
# だからmethods=[]これはリストになってる
# DevToolesのNetworkのとこから送られたformの中身が見れる
@app.route('/confirm', methods=['post'])
def confirm():
    # Formデータは、request.formから取得する
    # 全般request.argsと一緒。

    # フォームデータ(単一値)の取得
    id = request.form.get('id')

    # 必須チェック(Noneや、空の場合があるから)
    if not id:
        return 'ID必須' # 本来はリダイレクト
    
    # フォームデータ(複数値)の取得
    check = request.form.getlist('check')

    # 空チェック
    if not check:
        # エラーとする場合にはエラー処理を。
        pass

    return render_template('confirm.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)