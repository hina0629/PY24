# Flaskでは、同一エンドポイントにて、
# 以下のように構成するのが代表的。
# ・GET・・・画面表示
# ・POST・・・実処置
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# methodsでGET,POSTの両方を受け付ける
@app.route("/", methods=['get', 'post'])
def index():
    # request.methodで、GETとPOSTの
    # 処理を切り分けることが出来る
    if request.method == 'GET': # ここは大文字限定。
        return render_template('index.html')
    else:
        id = request.form.get('id')

        # 入力チェック
        if not id:
            return redirect(url_for('index'))

    # 入力チェックOKならDB登録etc...
    # その後、リダイレクト
    # リダイレクト先は、以下2つが一般的
    # ・自ページ
    # ・完了ページ


    # 確認画面を設ける場合もリダイレクトにて実装
    # ※要session
    
        return "登録完了"

if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)