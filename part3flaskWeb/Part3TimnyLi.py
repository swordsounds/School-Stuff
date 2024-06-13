#INSTRUCTIONS
#Create a venv or folder
#Inside the venv or folder, put the 2 html files (submit.html and form.html) into a folder named templates
#Put this python script into the venv or folder, rename it to app.py, or not its up to you
#Run script locally on editor and have fun!!!
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/form')
def ThisIsAForm():
    return render_template('form.html')

@app.route('/submit')
def ThisIsSubmit():
    return render_template('submit.html')
    
if __name__ == '__main__':
    app.run(debug=True)
