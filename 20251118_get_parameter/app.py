# リダイレクト
#  /aにアクセスしたのに、/bにアクセスしていた。
#  といった様に、ブラウザのリクエストURLを変更することが出来る。
#  これはHTTPの仕様で、本来はサイト移転時の対応が目的であり、リダイレクトと呼ばれる。
#   例）新サイトOpen！　旧サイトから切り替えたいけど、
# 　　　ユーザーは旧サイトのURLでアクセスしてくる。。。
#      じゃぁ、旧サイトにアクセスしてきたら、
#      新サイトのURLにアクセスするようにさせよう！
#      　→リダイレクト
# [リダイレクトの流れ] ※B…ブラウザ。S…サーバー。
#  ①BがSにリクエストを投げる。
#  ②Sがレスポンスを返すが、その際、移転したので、別URLに再度アクセスし直すように指示。
#  ③Bがレスポンスを受け取ると、指示通りのURLにリクエストを投げる。
#  ④SはBにレスポンスする。
#
#  →1回のリクエストの様に見えるけど、2回のリクエストとレスポンスが発生している。
#
# [サーバー目線でリダイレクトを一言で説明]
#  クライアントに、要求し直させる仕組み。
#
# [用途]
#  ①サイト切り替えの際に用いる。※冒頭の例。
#  ②エラーとなった際に、エラーページに飛ばす。
#  ③ログイン認証後に、特定のページに飛ばす。
#  ④セッションタイムアウト後に、ログインページに飛ばす。
#  ⑤PRG(Post Redirect Get)パターン等々。

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route('/new')
def new():
    return render_template('new.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)