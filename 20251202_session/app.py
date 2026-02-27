# Session
#  一般的には、一連の通信の始まりから終わりまでを指す。
#  端的に言うとログイン状態の実現。
# [仕組み]
#  ①サーバーサイドにてセッションID(乱数)を生成し、
#   Cookieにてクライアントへ受け渡す。
#  ②クライアントは再リクエスト時に、セッションIDを渡す(Cookie)。
#  以上の流れから、サーバーサイドは、②のリクエストは①のユーザーであることが分かる。
# [情報の保存先]
#  セッション領域と呼ばれる、ユーザー専用のデータ保存領域があり、
#  サーバーサイドに保存される。
#  １つの例としては、セッションIDをファイル名として、
#  ユーザー専用のデータ保存領域を確保する。
#  サーバーサイドにデータが保存されるので、セキュリティが保たれる。
#  以上が一般的なセッションの仕組み。
#
#  Flaskのセッション
#  一般とは異なり、デフォルトのFlaskではサーバーサイドに情報を保持せず、
# "全てのセッション情報をCookieで管理"する。
# secure cookieと呼ばれ、SECRET_KEYで暗号化されて保存される。
# ※情報漏洩の危険性があるため、機密情報は保持しないこと。
# ※また、cookieのため、保存データ量の上限がある。
# ※Flask-Sessionという拡張ライブラリを用いれば、サーバーサイドに保存も可能となる。

from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = '121790db709eab72b37ad987b96f48ffd2a5c57ad06eb51456fc2b0f42e7c2cf'
# py -c 'import secrets;print(secrets.token_hex())' # Flack officialより
# SECRET_KEYは、セッション情報暗号化のキー。セッション利用時はこの設定が必須。
# print(app.config) で、設定情報一覧が確認できる。

# print(app.config)

# セッションの有効期限変更
app.permanent_session_lifetime = timedelta(seconds=50)

@app.route("/")
def index():
    return render_template('index.html')

# セッション開始用のエンドポイント
@app.route("/start_session")
def start_session():
    # セッションの永続化
    # ※これを設定しないと、ブラウザを閉じたときに、
    #    セッションもcloseする。
    session.permanent = True

    session['id'] = 456
    return redirect(url_for('index'))

@app.route("/check_session")
def check_session():
    # セッションからデータを取得するには
    # session.get
    id = session.get('id')
    print(id)
    return redirect(url_for('index'))

@app.route("/end_session")
def end_session():
    # 個別削除には、session.popを用いる
    session.pop('id', None)
    # 第２引数は、無い場合の戻り値。
    # 第２引数の指定がなく、キーが存在しない場合、エラーになる

    # セッションの全削除はclear
    # 一般的にはログアウトで使われる
    session.clear()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)