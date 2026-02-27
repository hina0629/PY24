from flask import Flask, render_template, redirect, url_for, request, session, make_response
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '06bfef7dc49ffb7019f61c88d7c8c0a19d536fb68d712d6e74fe87460cb89161'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/ex1', methods=['GET', 'POST'])
def ex1():
    if request.method == 'POST':
        id = request.form.get('id')

        if id:
            response = make_response(redirect(url_for('ex1_completion')))

            response.set_cookie('id', id)

            return response
    return render_template('ex1.html')

# @app.route("/ex1_completion")
# def ex1_completion():
#     return render_template('ex1_completion.html')

@app.route("/ex1_completion", methos=['POST'])
def ex1_completion():
    return render_template('ex1_completion.html')

@app.route("/ex2")
def ex2():
    id = request.cookies.get('id', default='None')
    return render_template(
        'ex2.html',
        id=id
        )

# @app.route("/ex3")
# def ex3():
#     response = make_response(redirect(url_for('ex3_completion')))
#     response.delete_cookie('id')
#     return response

# @app.route("/ex3_completion")
# def ex3_completion():
#     return render_template('ex3.html')

@app.route("/ex3")
def ex3():
    id = request.cookies.get('id')
    if id:
        response = make_response(redirect(url_for('ex3')))
        response.delete_cookie('id')
        return response
    return render_template('ex3.html')

@app.route("/ex4")
def ex4():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name', 'abc')
    response.set_cookie('style', 'black')
    return response

@app.route("/ex5")
def ex5():
    name = request.cookies.get('name', default='')
    style = request.cookies.get('style', default='')
    return render_template(
        'ex5.html',
        name=name,
        style=style
        )

@app.route("/ex6")
def ex6():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('name')
    response.delete_cookie('style')
    return response

@app.route("/ex7", methods=['GET', 'POST'])
def ex7():
    if request.method == 'POST':
        id = request.form.get('user_id')
        session['id'] = id
        return redirect(url_for('ex7'))
    return render_template('ex7.html')

@app.route("/ex9")
def ex9():
    session.clear()
    return redirect(url_for('ex7'))

@app.route('/option1', methods=['GET', 'POST'])
def option1():
    if request.method == 'POST':
        id = request.form.get('user_id')

        if id:
            response = make_response(redirect(url_for('option1')))

            response.set_cookie('user_id_cookie', id)

            return response
        return redirect(url_for('option1'))
        
    id = request.cookies.get('user_id_cookie', default='')

    return render_template(
        'option1.html',
        id=id
        )

@app.route("/option2", methods=['GET', 'POST'])
def option2():
    session_list = session.get('session_list', [])

    if request.method == 'POST':
        memo = request.form.get('memo')

        if memo:
            session_list.append(memo)

        session['session_list'] = session_list

        return redirect(url_for('option2'))

    return render_template(
        'option2.html',
        session_list=session_list
        )

if __name__ == '__main__':
    app.run('0.0.0.0' , 80 , True)