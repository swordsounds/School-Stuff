# Simplified Lab Outline
# Part 1: Setting Up Your Flask App
# Install Flask and create a basic Flask application in app.py.
# Run a simple app that returns "Hello, World!" on the home page.
# Part 2: Creating Simple Dynamic Routes
# 1) First Dynamic Route:
#  Create a route /hello/<name> that greets the user by name.
# 2) Number Route:
#  Add a route /number/<int:n> that displays the number back to the user.|
# 3) Simple Greeting Page:
#  Create a route /greet that uses a query parameter name to display a greeting. If no name is
# given, it defaults to "Guest".
# Part 3: Introduction to Templates
# Basic Template Rendering:
#  Create a templates folder and add a simple hello.html template.
#  Modify the /hello/<name> route to render the hello.html template instead of returning a
# string.
# Part 4: Final Dynamic Route and Wrap-Up
#  Farewell Route:
# o Add a dynamic route /farewell/<name> that says goodbye to the user.
# o Use a simple template to render the farewell message.

from markupsafe import escape 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="http://127.0.0.1:5000/hello/Jake">Hello</a>\n<a href="http://127.0.0.1:5000/number/123">Number</a>\n' 

@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hello, {}!</h1>'.format(escape(name))

@app.route('/number/<int:n>')
def number(n):
    return '<h1>{}</h1>'.format(n)

@app.route('/greet/<name>')
def greeting(name):
    name = request.form.get('name')
    return '<h1>Hello, {}!</h1>'.format(escape(name))
@app.route('/farewell/<name>')
def farewell(name):
    user = {'username: <name>'}
    return render_template('bye.html', title='Goodbye', user=user)

if __name__ == '__main__':
    app.run(debug=True)