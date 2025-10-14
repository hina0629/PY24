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