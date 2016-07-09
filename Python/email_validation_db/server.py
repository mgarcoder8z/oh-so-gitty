from flask import Flask, request, redirect, render_template, session, make_response, flash
from mysqlconnection import MySQLConnector
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    query = "SELECT * FROM email_addresses"
    emails_list = mysql.query_db(query)
    return render_template('index.html', all_emails=emails_list)

@app.route('/create', methods=['POST'])
def create():
    session['email'] = request.form['email']
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        resp = make_response(render_template('results.html', message='message'))
        return resp

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        resp = make_response(render_template('results.html', message='message'))
        return resp
    else:
        #query = "INSERT INTO emails (email_addresses, created_at, updated_at) VALUES (:email_addresses, NOW(), NOW())"
        query = "INSERT INTO `emails`.`email_addresses` (`email_addresses`, `created_at`, `updated_at`) VALUES (:email_addresses, NOW(), NOW())"
        data = {
                 'email_addresses': request.form['email']
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        flash("The email you entered is a valid email address. Thank you!")
        resp = make_response(render_template('results.html', email = request.form['email'], message='message'))
        return resp

@app.route('/delete', methods=['POST'])
def remove_email(email_id):
    query = "DELETE FROM `emails`.`email_addresses` WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
