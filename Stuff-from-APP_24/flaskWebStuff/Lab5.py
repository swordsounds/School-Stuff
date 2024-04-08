from markupsafe import escape 
from flask import Flask, request, render_template

#Initialized the application
app = Flask(__name__)

# Simple app that returns "Hello, World!" on the home page.
@app.route('/')
def home():
    #Home route to display Hello World! in a heading one
    return '<h1>Hello World!</h1>' 

# Simple Dynamic Routes
# Created a route /hello/<name> that greets the user by name.
@app.route('/hello/<user>')
def hello(user):
    # Modified the /hello/<name> route to render the hello.html template instead of returning a
    # string.
    return render_template('hello.html', user=user)

#  Route /number/<int:n> that displays the number back to the user
@app.route('/number/<int:n>')
def number(n):
    return '<h1>{}</h1>'.format(n)

# Created a route /greet that uses a query parameter name to display a greeting.
#  If no name is given, it defaults to "Guest".
@app.route('/greet', defaults={'name': 'guest'})
@app.route('/greet/<name>')
def greeting(name):
    return render_template("simpleGreetingPage.html", user=name)

# Farewell Route:
# Added a dynamic route /farewell/<name> that says goodbye to the user.
@app.route('/farewell/<name>')
def farewell(name):
    # Simple template to render the farewell message.
    return render_template('bye.html', user=name)

#If the file is the main file, if will call the app
if __name__ == '__main__':
    app.run(debug=True)