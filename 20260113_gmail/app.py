# [前準備]※Gmail側の設定
# ①Googleアカウントログイン。
# ②2段階認証プロセスの有効化。
#  Googleアカウントの管理→セキュリティ→２段階認証プロセス
# ③アプリパスワードの発行。
#  上記2段階認証プロセスの画面の一番下に、
#  アプリパスワードが新たに出来ているので、そこで作成。
# ※アプリパスワードが無い場合、以下の直リンクで。
#  https://myaccount.google.com/apppasswords
# [注意]
# 1.PROXYを介すと、同一IPからか、全員による送信が不能となる。
#  ※若干名(4,5名)送信成功し、その後失敗。しばらく時間を時間を空ければOK。
# 2.ASCIIの文字コードエラーが出る場合、
#  PC名に全角を用いているのが原因。
# pip install flask flask-mail
from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587                       # TLSは587、SSLなら465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'hina.0629.xxx@gmail.com'   # 自身のGmailアカウント
app.config['MAIL_PASSWORD'] = 'xavj xxhy uixt tdsp'          # GmailのApp用のパスワード設定をしておく必要あり(半角スペース込みでOK)
app.config['MAIL_DEFAULT_SENDER'] = 'example@gmail.com'    # これを設定するとsender(差出人)設定が不要になる。ただしGmailでは生きない。※GamilのfromはMAIL_USERNAME
mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        # To
        recipients = ['hina.0629.xxx@gmail.com'] # recipients:受信者

        # メッセージ作成
        msg = Message('Test Mail', recipients, 'test message')

        # 送信
        mail.send(msg)

        # Messageは、コンストラクタではなく、プロパティによる設定も可能
        # msg = Message()
        # msg.subject = 'Test Mail'
        # msg.recipients = recipients
        # msg.body = "Hello Flask message sent from Flask-Mail"
        # msg.sender = "MAIL_DEFAULT_SENDERを設定していない場合、この設定が必須。"

        return 'OK'

if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)