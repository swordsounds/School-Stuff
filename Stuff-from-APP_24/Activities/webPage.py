from markupsafe import escape 
from flask import Flask

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
    return b

app = Flask(__name__)
@app.route('/')
def hello():
    return "<h1>I love you</h1>"

@app.route('/about/')
def about():
    return "<h3>I love you too</h3>"

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
@app.route('/add/<int:n1>/<int:n2>//')
def add(n1, n2):
    return '<h1>{}</h1>'.format(n1 + n2)
@app.route('/fib/<int:n>')
def show_fibonnaci(n):
    result = fibonacci(n)
    return (f'the fibonnaci number at {n} is {result}')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000) #specify port if running on other than port 80

