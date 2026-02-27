from flask import Flask, render_template, request, make_response, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = '68f88e75ef842fa22d998b78f7318b3c9d2c9b7d0bd51434f526e45b48b083b3'
# py -c 'import secrets;print(secrets.token_hex())'

USERS = [
    {'id':'a', 'password':'aaa'},
    {'id':'b', 'password':'bbb'},
    {'id':'c', 'password':'ccc'},
]

class Certification:
    def __init__(self, users):
        self.users = users

    def certification(self, user_id, password):
        for user in self.users:
            if user['id'] == user_id:
                if user['password'] == password:
                    return True
                
        # trueかfalseか
        return False

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if not session.get('id'):
            flash('ログインしてください')
            return redirect(url_for('login'))
        
        result = func(*args, **kwargs)
        return result
    return wrapper

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')

        if not id:
            flash("IDは必須入力です")
        elif not password:
            flash("Passwordは必須入力です")
        else:
            certification = Certification(USERS)

            user = certification.certification(id, password)
            
            if user:
                session['id'] = id
                return redirect(url_for('mypage'))
            else:
                flash('IDまたはパスワードが違います')
        return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route('/mypage', methods=['GET', 'POST'])
@login_required
def mypage():
    return render_template('mypage.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
