# テーブル結合検証
from sqlalchemy import event, create_engine, String, ForeignKey
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from typing import List

# 外部キー制約を有効にするためのコード
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
# SQLiteでは、外部キー制約が既定でOFFとなっている。

# engineの作成(DB接続の必要情報定義)
engine = create_engine(
    'sqlite:///py24.db',
    echo=True
)

# モデルの元クラスを作成
class Base(DeclarativeBase):
    pass

# Baseクラスを継承して、
# テーブル用のクラスを定義する
class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))

    # リレーションシップの定義
    # ユーザーが複数の注文をもつ「一対多」の関係を定義
    orders: Mapped[List['Order']] = relationship(back_populates='user')

class Order(Base):
    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    amount: Mapped[int]

    # リレーションシップの定義
    # 注文が１人のユーザーに属する「多対一」の関係を定義
    user: Mapped['User'] = relationship(back_populates='orders')

# relationship
# 外部キーの定義だけでなく、双方での関係(relationship)を設定することにより、
# よりコードが簡潔に書けるようになるため、SQL Alchemyとしての推奨事項となっている。
# （例：user.ordersや、order.userのような取得が行える）

# テーブルの生成
Base.metadata.create_all(bind=engine)

# ユーザー登録
# with Session(engine) as session:
#     for name in ['a', 'b', 'c']:
#         user = User(name=name)
#         session.add(user)
#         session.commit()

# 外部キー検証(存在しないユーザーIDでは登録できない)
# with Session(engine) as session:
#     order = Order(user_id=10, amount=2)
#     session.add(order)
#     session.commit()

# オーダー登録(存在するユーザーIDで登録できること)
# with Session(engine) as session:
#     ids = [1,1,2,3,2]
#     amounts = [10,20,50,40,10]
#     for id, amount in zip(ids, amounts):
#         order = Order(user_id=id, amount=amount)
#         session.add(order)
#         session.commit()

# 取得
with Session(engine) as session:
    users = session.query(User).all()
    for user in users:
        print(f'User {user.id} = {user.name}')

        # relationship を設定しているので、
        # 以下コードで関連先を取り出すことができる。
        for order in user.orders:
            print(f'  Order {order.id} : amount={order.amount}')
            # echo=Falseにしたら実行結果が見やすくなる
        
        # user.orders で都度SQLが実行される→N+1問題

# 取得(一括取得)※JOINが用いられるので、
# こっちのほうが早い(N+1問題の解消)
from sqlalchemy.orm import joinedload

with Session(engine) as session:
    users = session.query(User).options(joinedload(User.orders)).all()
    for user in users:
        print(f'User {user.id} = {user.name}')
        for order in user.orders:
            print(f'  Order {order.id} : amount={order.amount}')