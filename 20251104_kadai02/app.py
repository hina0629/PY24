from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html'
    )

@app.route('/ex1')
def ex1():
    import random
    number = random.randint(1,3)
    return render_template(
        'ex1.html',
        number=number
    )

@app.route('/ex2')
def ex2():
    import random
    number = random.randint(1,3)
    return render_template(
        'ex2.html',
        number=number
    )

@app.route('/ex3')
def ex3():
    import random
    number = random.randint(1,3)
    return render_template(
        'ex3.html',
        number=number
    )

@app.route('/ex4')
def ex4():
    import random
    numbers = []
    for i in range(100):
        number = random.randint(1,10)
        numbers.append(number)
    
    return render_template(
        'ex4.html',
        numbers=numbers
    )

@app.route('/ex5')
def ex5():
    import random
    numbers = []
    for i in range(100):
        number = random.randint(1,10)
        numbers.append(number)
    
    return render_template(
        'ex5.html',
        numbers=numbers
    )

@app.route('/ex6')
def ex6():
    return render_template(
        'ex6.html'
    )

@app.route('/ex7')
def ex7():
    from product import Product
    products = [
        Product(1, 'a', 100, 'daikichi'),
        Product(2, 'b', 200, 'kichi'),
        Product(3, 'c', 300, 'kyo')
        ]
    return render_template(
        'ex7.html',
        products=products
    )

@app.route('/option1')
def option1():
    from product import Product
    products = [
        Product(1, 'a', 100, 'daikichi'),
        Product(2, 'b', 200, 'kichi'),
        Product(3, 'c', 300, 'kyo')
        ]
    return render_template(
        'option1.html',
        products=products
    )

@app.route('/option1_2')
def option1_2():
    from product import Product
    products = []
    return render_template(
        'option1.html',
        products=products
    )

@app.route('/option2')
def option2():
    return render_template(
        'option2.html',
    )

if __name__ == '__main__':
    app.run('0.0.0.0', 80, True)