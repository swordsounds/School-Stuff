from markupsafe import escape 
from flask import Flask, request, render_template

app = Flask(__name__)

# simple app that returns "Hello, World!" on the home page.
@app.route('/')
def home():
    return '<h1>Hello World!</h1>\n<a href="http://127.0.0.1:5000/hello/Jake">Hello</a>\n<a href="http://127.0.0.1:5000/number/123">Number</a>\n<a href="http://127.0.0.1:5000/farewell/">Farewell</a>\n<a href="http://127.0.0.1:5000/greet/">Greet</a>' 

# Part 2: Creating Simple Dynamic Routes
# Create a route /hello/<name> that greets the user by name.
@app.route('/hello/<user>')
def hello(user):
    # Modify the /hello/<name> route to render the hello.html template instead of returning a
    # string.
    return render_template('hello.html', user=user)

#  route /number/<int:n> that displays the number back to the user
@app.route('/number/<int:n>')
def number(n):
    return '<h1>{}</h1>'.format(n)

# Create a route /greet that uses a query parameter name to display a greeting. If no name is
# given, it defaults to "Guest".
@app.route('/greet?user=')
def greeting():
    user = request.args.get('name')
    return render_template("simpleGreetingPage.html", user=user)

#  Farewell Route:
# o Add a dynamic route /farewell/<name> that says goodbye to the user.
# o Use a simple template to render the farewell message.
@app.route('/farewell/<name>')
def farewell(name):
    user = request.args.get('name')
    return render_template('bye.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)