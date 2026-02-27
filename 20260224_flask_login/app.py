# pip install flask flask-login flask-sqlalchemy
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import select, String, Integer
from werkzeug.security import generate_password_hash, check_password_hash
# werkzeug(ヴェルクツォイク)はflaskの依存ライブラリ。

# SQLAlchemyのインスタンス化
db = SQLAlchemy()

# LoginManagerのインスタンス化
login_manager = LoginManager()

# ユーザーモデル定義
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    # nullable NULL許容
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)


def register_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        else:
            email = request.form['email']
            name = request.form['name']
            password = request.form['password']
            password_confirmation = request.form['password_confirmation']

            # パスワードの一致確認
            if password != password_confirmation:
                error_message = 'パスワード不一致'

                # 入力エラー系は、render_templateにて、
                # 入力値を復元するのが一般的
                # パスワードと確認用パスワードが違ったときに入力したemailとnameが消えないように。
                return render_template('signup.html', email=email, name=name, error_message=error_message)
            
            # メールアドレスの重複確認（簡易版。ほんとはtryとかを使う）
            # stmt ステートメント → SQL文で書かれた命令文
            stmt = select(User).where(User.email == email)
            # scalar 一次元配列にする。あっても1件しかないから
            existing_user = db.session.scalar(stmt)

            # メールアドレスが既に存在していた場合
            if existing_user:
                error_message = 'emailは既に使われています'

                # 入力エラー系は、render_templateにて、
                # 入力値を復元するのが一般的
                # 何のemailがエラーかわかるようにemailも復元
                return render_template('signup.html', email=email, name=name, error_message=error_message)

            # パスワードのハッシュ化
            hashed_password = generate_password_hash(password)

            # 新しいユーザーをDBに保存
            user = User(email=email, password=hashed_password, name=name)

            db.session.add(user)
            db.session.commit()

            flash('ユーザー作成に成功しました。', 'success')
            return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        else:
            email = request.form['email']
            password = request.form['password']

            # ユーザー情報の取得
            stmt = select(User).where(User.email == email)
            # scalar 一次元配列にする。あっても1件しかないから
            user = db.session.scalar(stmt)

            if user and check_password_hash(user.password, password):
                # セッション固定攻撃の対策
                session.clear()

                # 認証成功を記録
                login_user(user)
                
                return redirect(url_for('dashboard'))
            else:
                flash('emailまたはpasswordが不正です')
                return render_template('login.html', email=email)

    # ダッシュボード
    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template('dashboard.html')

    # ログアウト
    @app.route('/logout')
    @login_required
    def logout():
        # ログアウト処理
        logout_user()
        return redirect(url_for('login'))

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'asdfghjkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"

    # SQLAlchemyとflaskの関連付け
    db.init_app(app)

    # LoginManagerとflaskの関連付け
    login_manager.init_app(app)

    login_manager.login_view = "login"
    # ↑ログイン必須ページに、未ログイン状態のアクセスが
    # なされた時の、リダイレクト先（エンドポイント名）
    # ※これを設定しないと、既定のエラーメッセージが表示される。

    # おまじない
    # ログインユーザーを取得するための関数(必須)
    # この関数は、flask内部から呼ばれている。
    @login_manager.user_loader
    def load_user(id):
        return db.session.get(User, int(id))

    # ルーティングの登録
    register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # なければ作る。
        db.create_all()

    app.run('0.0.0.0', 80, True)