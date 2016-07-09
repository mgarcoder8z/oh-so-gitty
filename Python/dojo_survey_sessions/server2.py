from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index2.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/user', methods=['POST'])
def create_user():
  #print "Got Post Info"
   # notice how the key we are using to access the info corresponds with the names of
   # of the inputs from our html form
   # here we add two properties to session to store the name and email
  session['name'] = request.form['name']
  session['location'] = request.form['location']
  session['language'] = request.form['language']
  session['comments'] = request.form['comments']
  return redirect('/result')
@app.route('/result')
def show_user():
  return render_template('user.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])
app.run(debug=True) # run our server
