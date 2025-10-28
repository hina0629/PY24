# テンプレートエンジン
#  HTMLを中心に、動的なページを作成する仕組み。
#  Flaskでは、Jinja2というテンプレートエンジンを利用。
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # HTMLファイルを読み込んで返却。
    return render_template('index.html')

    # テンプレート(HTML)ファイルは、「templates」フォルダに配置する必要がある。
    # MVTモデル
    #  M(Model)…業務ロジックを担当
    #  V(View)…入力を受け取り、ModelとTemplateの制御を担当
    #  T(Template)…入出力画面を担当
    # ちなみに、当ファイルはVになる。
    # おまけ。MVCと対応すると、V=C, T=Vになる。

# Pythonから、テンプレートファイルに、データを引き渡すことができる。
@app.route('/pass_data')
def pass_data():
    # 第二引数以降に、名前付き引数で渡す。
    return render_template(
                            'pass_data.html',
                            id=123,
                            name='<h2>abc</h2>'
                            )

# if for
@app.route('/if_for')
def if_for():
    age = 20
    colors = ['r', 'g', 'b']
    colors_dic = {
        'r':'赤',
        'g':'緑',
        'b':'青'
    }

    # userモジュールからUserクラスを取得
    from user import User
    # ↓ sqlalchemyのselectで持ってきたときも同じ感じになる
    users = [
        User(1,'a'),
        User(2,'b'),
        User(3,'c')
        ]

    return render_template(
                            'if_for.html',
                            age=age,
                            colors=colors,
                            colors_dic=colors_dic,
                            users = users
                            )

# img/js/css
@app.route('/img_etc')
def img_etc():
    return render_template('img_etc.html')

# コンポーネント
# ctrl + d で同じやつ一気に選択して変えられる
# 変え終わったらEscでぬける
@app.route('/component')
def component():
    return render_template('component.html')

# レイアウト継承
@app.route('/extends')
def extends():
    return render_template('extends.html')

# if for
@app.route('/filter')
def filter():
    age = 20
    colors = ['r', 'g', 'b']

    return render_template(
                            'filter.html',
                            age=age,
                            colors=colors,
                            )

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)