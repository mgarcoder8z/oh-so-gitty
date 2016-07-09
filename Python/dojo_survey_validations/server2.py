from flask import Flask, render_template, request, redirect, session, flash
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
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    if len(request.form['name']) < 1:
        flash("ERROR: Name cannot be empty, please enter a name!") # just pass a string to the flash function
    else:
        flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function

    if len(request.form['comments']) > 1 < 120:
        flash("Thank you for your comments")
    else:
        flash("ERROR: Comments cannot be empty!")

    if len(request.form['comments']) > 120:
        flash("ERROR: Comments cannot exceed 120 characters")
    else:
        flash("Please keep your comments under 120 characters")

    return redirect('/result')

@app.route('/result')
def show_user():
  return render_template('result.html', name=session['name'], location=session['location'], language=session['language'], comments=session['comments'])

app.run(debug=True) # run our server
