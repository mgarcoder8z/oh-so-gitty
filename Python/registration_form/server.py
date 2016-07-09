# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']

    # if first_name is empty,
    if len(session['first_name']) < 1:
        flash('First name cannot be blank')
    # if first_name contains symbol(s) or numberic value(s),
    elif str.isalpha(str(session['first_name'])) == False:
        flash('First name cannot contain symbol(s) or number(s)!')
    else:
        flash("Success!")

    # if last_name is empty,
    if len(session['last_name']) < 1:
        flash('Last name cannot be blank')
    # if first_name contains symbol(s) or numberic value(s),
    elif str.isalpha(str(session['last_name'])) == False:
        flash('Last name cannot contain symbol(s) or number(s)!')
    else:
        flash("Success!")

    if len(session['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        flash("Success!")

    if len(session['password']) < 1:
        flash("Password cannot be blank!")
    elif not(session['password']) < 8:
        flash("Password must be more than 8 characters")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        flash("Success!")

    if len(session['confirm']) < 1:
        flash("Confirmation cannot be blank!")
    elif not (session['password']) == (session['confirm']):
            flash("Password and Confirmation must match")
    # else if email doesn't match regular expression display an "invalid email address" message
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)
