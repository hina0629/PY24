from flask import Flask, render_template, request, make_response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'e9c02086690c22ae01ab6228f00820f3672d6e7432113b6c3b463bf505e74166'
# app.config['SECRET_KEY']の別ver

# py -c 'import secrets;print(secrets.token_hex())' # Flack officialより

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ex1_set_cookie')
def ex1_set_cookie():
    return render_template('ex1_set_cookie.html')

@app.route('/ex1_finish', methods=['post'])
def ex1_finish():
    response = make_response(
        render_template('ex1_finish.html')
    )

    response.set_cookie('id', request.form.get('id'))

    return response

@app.route('/ex2_check_cookie')
def ex2_check_cookie():
    cookie_id = request.cookies.get('id')

    return render_template('ex2_check_cookie.html', cookie_id=cookie_id)

@app.route('/ex3_delete_cookie')
def ex3_delete_cookie():
    response = make_response(
        render_template('ex3_delete_cookie.html')
    )

    response.delete_cookie('id')

    return response

@app.route('/ex4_set_cookies')
def ex4_set_cookies():
    response = make_response(
        redirect(url_for('index'))
    )

    response.set_cookie('name', 'abc')
    response.set_cookie('style', 'black')

    return response

@app.route('/ex5_view_cookies')
def ex5_view_cookies():
    return render_template('ex5_view_cookies.html', cookies=request.cookies)

@app.route('/ex6_delete_cookies')
def ex6_delete_cookies():
    response = make_response(
        redirect(url_for('index'))
    )

    response.delete_cookie('name')
    response.delete_cookie('style')

    return response

@app.route('/ex7_session', methods=['get', 'post'])
def ex7_session():
    if request.method == 'POST':
        session['id'] = request.form.get('id', '')
        return redirect(url_for('ex7_session'))
    
    return render_template('ex7_session.html')

@app.route('/ex9_delete_session')
def ex9_delete_session():
    session.clear()
    return redirect(url_for('ex7_session'))

@app.route('/option1', methods=['get', 'post'])
def option1():
    if request.method == 'POST':
        response = make_response(
            redirect(url_for('option1'))
        )

        response.set_cookie('id', request.form.get('id', ''))
        return response
    
    return render_template('option1.html')

@app.route('/option2', methods=['get', 'post'])
def option2():
    # if 'memo' not in session:
    #     session['memo'] = []

    if request.method == 'POST':
        session.modified = True
        # session['memo'].append(request.form.get('text', ''))

        # 上のコメント(3)行が、この1行で行ける。
        session.setdefault('memo', []).append(request.form.get('text', ''))

        return redirect(url_for('option2'))
    
    return render_template('option2.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
