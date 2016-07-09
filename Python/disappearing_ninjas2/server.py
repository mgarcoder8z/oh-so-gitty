from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninja')
def all_ninjas():
    displayAll = True
    return render_template('result.html', displayAll=displayAll)

@app.route('/ninja/<color>')
def get_ninja_color(color):
    # show the turtle profile for that color in URL

    displayAll = False
    return render_template('result.html', color=color, displayAll=displayAll)

app.run(debug=True) # run our server
