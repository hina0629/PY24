# Cookie
#  クライアントサイドに情報を残す技術。
#
# [仕組み]
#  ①サーバーサイドにて、HTTPレスポンスヘッダに、key=valueの形でデータを積む。
#  ②クライアント(ブラウザ)にて、key=valueを保存する。
#  ③サーバーに再要求(リクエスト)時、key=valueをHTTPリクエストヘッダに積む。
#  ④サーバーサイドにて、keyを指定してデータを引っこ抜く。※①のvalueを復元することができる。
# [Point!]
#  クライアントサイドに保存された情報は、再リクエスト時に自動的に送信される。
# [注意事項]
#  データサイズに上限がある。約4KB。
#  データ漏洩の危険性がある。(機密情報は保持しない様にする。)
# [用途]
#  ・セッション管理…セッションIDを保存し、繋がっている状態を実現する。
#  ・設定情報の保存…ユーザーの設定情報を保存し、次回に適用する。
#  ・トラッキング…ユーザーのブラウジング行動を保存し、追跡出来るようにする。
#  ・CSRF(クロスサイトリクエストフォージェリ)対策 等々。

from flask import Flask, render_template, redirect, url_for, request, make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/set_cookie")
def set_cookie():
    # 有効期限を設定すれば、永続化可能。
    # ※既定は、ブラウザを落とすまで有効。
    expires = datetime.datetime.now( datetime.timezone.utc ) + datetime.timedelta(seconds=50)

    # レスポンスオブジェクト(イメージHTTPパケット)
    # を生成する。
    # 今までは勝手に作られてた(returnの先で作られてた)のを今回は自分で作る。
    response = make_response(redirect(url_for('index')))

    # Cookieを設定する。
    # ※Cookieは、HTTP Headerに設定される。
    # Headerをさわりたいからわざわざこうやっている。
    response.set_cookie('id', '123', expires=expires)

    return response

@app.route("/check_cookie")
def check_cookie():
    # Cookieは、存在する場合、自動で送信される。
    # ※HTTP Headerに積まれる。
    # Cookieを許可しますか？ -> パソコンに情報を保存していいかを聞いてる
    # サーバーサイドに保存すると容量がパンクするからクライアントサイドに保存

    # request.cookiesで取得
    # Noneがあり得るから危険
    print(request.cookies.get('id'))

    # 厳密にチェックする場合
    if 'id' in request.cookies:
        print(request.cookies.get('id'))

    # defaultを使ってNone対策をしてもよい
    print(request.cookies.get('id', default='0'))

    # Cookieはブラウザごと

    return render_template('check_cookie.html')

@app.route("/delete_cookie")
def delete_cookie():
    response = make_response(redirect(url_for('index')))

    response.delete_cookie('id')
    # 削除の仕組みは、
    # 有効期限を過去日付にしている。

    return response

if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)