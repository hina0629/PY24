from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from datetime import datetime

#SQLAlchemyのインスタンス化
db = SQLAlchemy()

class Product(db.Model):
  #flask-SQLAlchemyの場合この形
  __tablename__ = "product"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  price: Mapped[int] = mapped_column(Integer, nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

def create_app():
  app = Flask(__name__)

  app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///product.db"
  #flask-SQLAlchemyのdbファイルは、既定でinstanceフォルダに格納。
  
  #SQLAlchemyとflaskの関連付け
  db.init_app(app)

  #ルーティングの登録
  register_routes(app)

  return app

def register_routes(app):
  @app.route('/',methods=['GET','POST'])
  def index():
    #商品情報の取得
    products = Product.query.all() #flask-sqlalchemy独自の書き方
    return render_template('index.html',products=products)
  
  @app.route('/create',methods=['GET','POST'])
  def create():
    #商品情報の取得
    products = Product.query.all() #flask-sqlalchemy独自の書き方
    if request.method == 'GET':
      return render_template('create.html')
    else:
      name = request.form['name']
      price = int(request.form['price'])
      product = Product(name=name, price=price)

      db.session.add(product)
      db.session.commit()
      return redirect(url_for('index'))
    
  @app.route('/update/<int:id>',methods=['GET','POST'])
  def update(id):
    #対象データを取得する
    product = db.session.get(Product, id)

    if request.method == 'GET':
      return render_template('update.html', product=product)
    else:
      product.name = request.form['name']
      product.price = int(request.form['price'])

      db.session.commit()
      return redirect(url_for('index'))
    
  @app.route('/delete',methods=['POST'])
  def delete():
    id = int(request.form['id'])

    #対象データを取得する
    product = db.session.get(Product, id)

    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))

app = create_app()

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run('0.0.0.0',80,True)