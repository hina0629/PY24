from flask import Flask, render_template, request, flash, redirect, url_for, session
from login import Login

app = Flask(__name__)

app.secret_key = '30e803d7dea937c14e15c102332b431c622732e15729750ca25877ee4c38f68d'
# py -c 'import secrets;print(secrets.token_hex())'

login = Login()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['get','post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 入力値チェック
        id = request.form.get('id')
        if not id:
            flash('IDは必須入力です。')
            return redirect(url_for('login'))
        
        password = request.form.get('password')
        if not password:
            flash('Passwordは必須入力です。')
            return redirect(url_for('login'))
        
        # 認証処理
        is_authenticated = login.auth(id, password)

        if is_authenticated:
            session.clear() # Session Fixation 攻撃の防止(セッションIDの再生成)
            session['id'] = id
            endpoint = 'mypage'
        else:
            flash('IDまたはPasswordが異なります。')
            endpoint = 'login'

        return redirect(url_for(endpoint))


# @app.route('/mypage')
# def mypage():
#     if not session.get('id'):
#         flash('ログインしてください。')
#         return redirect(url_for('login'))

#     return render_template('mypage.html')

from functools import wraps
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('id'):
            flash('ログインしてください。')
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return wrapped_view

@app.route('/mypage')
@login_required
def mypage():
    return render_template('mypage.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
