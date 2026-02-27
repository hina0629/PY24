from flask import Flask, render_template
import random
from product import Product

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ex1')
def ex1():
    return render_template('ex1.html', rand=random.randint(1,3), rand_list=[1, 2, 3])

@app.route('/ex2')
def ex2():
    return render_template('ex2.html', rand=random.randint(1,3))

@app.route('/ex3')
def ex3():
    return render_template('ex3.html', rand=str(random.randint(1,3)))

@app.route('/ex4')
def ex4():
    return render_template('ex4.html', rand=[random.randint(1, 10) for _ in range(100)])

@app.route('/ex5')
def ex5():
    return render_template('ex5.html', rand=[random.randint(1, 10) for _ in range(100)])

@app.route('/ex6')
def ex6():
    return render_template('ex6.html')

@app.route('/ex7')
def ex7():
    products = []
    products.append(Product(1, 'a', 100, '1.png'))
    products.append(Product(2, 'b', 200, '2.png'))
    products.append(Product(3, 'c', 300, '3.png'))

    return render_template('ex7.html', products=products)

@app.route('/option1_ari', endpoint='option1_ari')
def option1():
    products = []
    products.append(Product(1, 'a', 100, '1.png'))
    products.append(Product(2, 'b', 200, '2.png'))
    products.append(Product(3, 'c', 300, '3.png'))

    return render_template('option1.html', products=products)

@app.route('/option1_nashi', endpoint='option1_nashi')
def option1():
    products = []

    return render_template('option1.html', products=products)

@app.route('/option2')
def option2():
    return render_template('option2.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)
