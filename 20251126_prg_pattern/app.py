# PRGパターン
# Post Redirect Get Pattern
# Postのままだと、更新時に不具合を起こすから
# Redirectして、POST要求からGET要求に
# 変更する手法
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/products/new')
def products_new():
    return render_template('products/new.html')

@app.route('/products', methods=['post'])
def products():
    id = request.form.get('id')

    # 入力値チェック 割愛

    # DB登録 割愛
    import datetime
    print(datetime.datetime.now())


    return render_template('products/create_complate.html') #ここで更新賭けたら二重購入になるからそれを防ぐ↓

@app.route('/products_prg/new')
def products_prg_new():
    return render_template('products_prg/new.html')

@app.route('/products_prg', methods=['post'])
def products_prg():
    id = request.form.get('id')

    # 入力値チェック 割愛

    # DB登録 割愛
    import datetime
    print(datetime.datetime.now())

    # return render_template('products_prg/create_complate.html')
    # リダイレクトして、POST要求をGET要求に変える
    return redirect(url_for('pcc')) #ProductCreateComplateの略

@app.route("/pcc")
def pcc():
    return render_template('products_prg/create_complate.html')



if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)