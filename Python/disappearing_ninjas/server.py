from flask import Flask, render_template, request, redirect, session, make_response, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/ninja')
def all_turtles():
     resp = make_response(render_template('all.html'))
     return resp

@app.route('/ninja/<ninja_color>')
def red_turtle(ninja_color=None):
    # show the turtle profile for that color in URL
    if ninja_color == 'red':
        resp = make_response(render_template('red.html', ninja_color='red'))
        return resp

    if ninja_color == 'blue':
        resp = make_response(render_template('blue.html', ninja_color='blue'))
        return resp

    if ninja_color == 'orange':
        resp = make_response(render_template('orange.html', ninja_color='orange'))
        return resp

    if ninja_color == 'purple':
        resp = make_response(render_template('purple.html', ninja_color='purple'))
        return resp



    else:
        resp = make_response(render_template('error.html'))
        return resp

app.run(debug=True) # run our server
