from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next')
def next():
    # クエリパラメータを取得するには、
    # request.argsを用いる

    # 単一値の取得(ラジオボタンとか<input type='text'>とか)
    # -------------------------------------------------- #
    # 方法その１
    id = request.args.get('id')

    # 取得できなければNoneが返る。
    id = request.args.get('id2')
    if id is None:
        id = 'None'

    # Noneの場合の固定値設定も可
    id = request.args.get('id2', default='none')

    # ちゃんとしたチェック処理を作ってみると．．．
    id = request.args.get('id')
    # ちゃんと渡ってきているかのチェック
    if not id:
        return 'IDは必須'

    # -------------------------------------------------- #
    # 方法その２
    id = request.args['id']

    # こっちの場合、取得できない場合はエラーとなる
    # id = request.args['id2'] -> BadRequestKeyError

    # -------------------------------------------------- #
    # 複数値の取得
    names = request.args.getlist('names')
    names = request.args.getlist('names2')
    # 取得できない場合は空のリスト
    
    # 空チェック
    if not names:
        return '空'
    
    return id + ''.join(names)

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)