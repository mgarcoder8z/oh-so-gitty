from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import os
import random
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['occupation'] = request.form['occupation']
    errors = []

    if len(session['first_name']) < 1:
    	errors.append("Please put your friend's first name!")
    elif str.isalpha(str(session['first_name'])) == False:
    	errors.append("No symbols or numbers are allowed as a first name!")
    if len(session['last_name']) < 1:
    	errors.append("Please put your friend's last name!")
    elif str.isalpha(str(session['last_name'])) == False:
    	errors.append("No symbols or numbers are allowed as a last name!")
    if len(session['occupation']) < 1:
    	errors.append("Please put your friend's occupation!")

    if errors:
    	for error in errors:
    		flash(error, 'error')
    	return redirect('/')
    else:
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'first_name': request.form['first_name'],
                 'last_name':  request.form['last_name'],
                 'occupation': request.form['occupation']
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id = :id"
	data = {'id': id}
	friend = mysql.query_db(query, data)
	return render_template('edit.html', one_friend = friend[0])

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['occupation'] = request.form['occupation']
    # Run query, with dictionary values injected into the query.
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = NOW() WHERE id = :id"
    data = {
    'first_name': str(session['first_name']), 'id': id,
    'last_name': str(session['last_name']), 'id': id,
    'occupation': str(session['occupation']), 'id': id
    }
    mysql.query_db(query, data)
    session.pop('first_name')
    session.pop('last_name')
    session.pop('occupation')
    flash('You have successfully added a friend to the list!', 'success')
    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    flash("Successfully deleted a friend from the list", 'success')
    return redirect('/')

app.run(debug=True)
