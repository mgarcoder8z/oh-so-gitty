from flask import Flask, request, redirect, render_template, session, make_response, flash
from datetime import datetime
import os
import random
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
bcrypt = Bcrypt(app)
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'vcharm')

@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        flash("Please log in for full functionality")

@app.route('/users', methods=['POST'])
def create():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']
    errors = []

    if len(session['first_name']) < 3:
    	errors.append("Please put your first name, at least 2 characters long")
    elif str.isalpha(str(session['first_name'])) == False:
        errors.append("First name field is required")

    if len(session['last_name']) < 3:
    	errors.append("Please put your last name, at least 3 characters long")
    elif str.isalpha(str(session['last_name'])) == False:
    	errors.append("No symbols or numbers are allowed as a last name!")

    if len(session['email']) < 1:
        errors.append("Email cannot be blank!")
    elif not EMAIL_REGEX.match(session['email']):
        errors.append("Invalid Email Address!")

    if len(session['password']) < 1:
        errors.append("Password cannot be blank!")
    elif not len(session['password']) > 8:
        errors.append("Password must be more than 8 characters")

    if len(session['confirm']) < 1:
        errors.append("Confirmation cannot be blank!")
    elif not (session['password']) == (session['confirm']):
        errors.append("Password and Confirmation must match")

    if errors:
    	for error in errors:
    		flash(error, 'error')
    	return redirect('/')

    else:
        pw_hash = bcrypt.generate_password_hash(session['password'])
        query = "INSERT INTO `vcharm`.`users` (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'first_name': str(session['first_name']),
                 'last_name':  str(session['last_name']),
                 'email': str(session['email']),
                 'pw_hash': pw_hash
               }
        mysql.query_db(query, data)
        session.clear()
        flash('You have successfully signed up, you can now Login', 'success')
        return redirect('/#How')

#@app.route('/show', methods=['GET'])
#def show():
    #query = "SELECT users FROM vcharm"                           # define your query
    #users = mysql.query_db(query)                           # run query with query_db()
#    return render_template('users.html', all_users=users) # pass data to our template


@app.route('/login', methods=['POST', 'GET'])
def login():
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    errors = []

    if len(session['password']) < 1:
        errors.append("Password cannot be blank!")
    elif not len(session['password']) > 8:
        errors.append("Password must be more than 8 characters")

    if len(session['email']) < 1:
        errors.append("Email cannot be blank!")
    elif not EMAIL_REGEX.match(session['email']):
        errors.append("Invalid Email Address!")

    if errors:
    	for error in errors:
    		flash(error, 'error')
    	return redirect('/#How')

    else:
     email = request.form['email']
     password = request.form['password']
     user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
     data = {'email': str(session['email'])}
     user = mysql.query_db(user_query, data)
     #query_data = { 'email': email }
     #user = mysql.query_db(user_query, query_data) # user will be returned in a list
     if bcrypt.check_password_hash(user[0]['pw_hash'], password) == True:
         session['id'] = user[0]['id']
         #session['name'] = user[0]['first_name']
         #session['name'] = user[0]['first_name'] + " " + user[0]['last_name']
         resp = make_response(render_template('login.html'))
         return resp
     else:
          # set flash error message and redirect to login page
         flash("Login Failed: Please recheck and reenter your username and/or password")
         return redirect('/#How')

@app.route('/messages', methods=['POST'])
def create_message():
    if session.get('logged_in') == True:
    	new_message = request.form['message']
    	escaped_new_message = new_message.replace("'", "\\'")
    	query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(session['id'], escaped_new_message)
    	data = {
                'user_id': session['id'],
                'message': request.form['message']
                }
    	mysql.query_db(query, data)
    	return redirect('/show')
    else:
        flash("Login is required")
        return redirect('/#How')


@app.route('/comments', methods=['POST'])
def create_comment():
    if session.get('logged_in') == True:
    	new_comment = request.form['comment']
    	message_id = request.form['message_id']
    	escaped_new_comment = new_comment.replace("'", "\\'")
    	query = "INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(message_id, session['id'], escaped_new_comment)
    	data =  {
                'message_id': request.form['message_id'],
                'user_id': session['id'],
                'comment': request.form['comment']
                }
    	mysql.query_db(query, data)
    	return redirect('/show')
    else:
        flash("Login is required")
        return redirect('/#How')

@app.route('/show', methods=['GET'])
def wall():
		# fetch_messages_query = "SELECT messages.id as message_id, messages.message, concat(users.first_name, ' ', users.last_name) as author_name, messages.created_at FROM messages LEFT JOIN users ON users.id = messages.user_id order by created_at desc"
	if session.get('logged_in') == True:
        query = "SELECT messages.id AS message_id, messages.message, CONCAT(users.first_name, ' ', users.last_name) AS author_name, messages.created_at, GROUP_CONCAT(comments.comment SEPARATOR '-----') AS comments, GROUP_CONCAT(CONCAT(users2.first_name, ' ', users2.last_name) SEPARATOR '-----') AS comment_author, GROUP_CONCAT(comments.created_at SEPARATOR '-----') AS comment_created_at FROM messages LEFT JOIN users ON users.id = messages.user_id LEFT JOIN comments ON messages.id = comments.message_id LEFT JOIN users AS users2 ON users2.id = comments.user_id GROUP BY messages.id ORDER BY created_at DESC"
		all_messages = mysql.query_db(query)
		for msg in all_messages:
			print '============'
			print msg
			print '============'
			msg['comments'] = str(msg['comments']).split('-----')
			msg['comment_author'] = str(msg['comment_author']).split('-----')
			msg['comment_created_at'] = str(msg['comment_created_at']).split('-----')
		print all_messages
		return render_template('login.html', all_messages=all_messages)
    else:
        flash("Login is required")
        return redirect('/#How')

@app.route('/messages/<id>/edit')
def edit(id):
    if session.get('logged_in') == True:
    	query = "SELECT * FROM messages WHERE id = :id"
    	data = {
                'id': id
                }
    	user_messages = mysql.query_db(query, data)
	    return render_template('edit.html', one_user = user_messages[0])
    else:
        flash("Login is required")
        return redirect('/#How')

@app.route('/messages/<id>', methods=['POST'])
def update(id):
    if session.get('logged_in') == True:
        session['message'] = request.form['message']
        query = "UPDATE `vcharm`.`messages` SET message = :message, updated_at = NOW() WHERE id = :id"
        data = {
                'id': id,
                'message': str(session['message'])
                }
        mysql.query_db(query, data)
        flash('You have successfully updated your message!', 'success')
        return redirect('/show')
    else:
        flash("Login is required")
        return redirect('/#How')


@app.route('/messages/<id>/delete', methods=['POST'])
def destroy(id):
    if session.get('logged_in') == True:
        query = "DELETE FROM `vcharm`.`messages` WHERE id = :id"
        data = {'id': id}
        mysql.query_db(query, data)
        session.clear()
        flash("Successfully deleted a post from the list", 'success')
        return redirect('/show')
    else:
        flash("Login is required")
        return redirect('/#How')

@app.route('/logout')
def logout():
     session.clear()
     flash('You have successfully logged out!')
     return redirect('/')
#@app.route('/users/<id>/delete', methods=['POST'])
#def destroy(id):
    #query = "DELETE FROM users WHERE id = :id"
    #data = {'id': id}
    #mysql.query_db(query, data)
    #flash("Successfully deleted a user from the list")
    #return redirect('/')

app.run(debug=True)
