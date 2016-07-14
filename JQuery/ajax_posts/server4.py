from flask import Flask, request, redirect, render_template, session, make_response, flash, jsonify
#from datetime import datetime
import os
import random
#import re
#EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
#from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = os.urandom(24)
#'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
#bcrypt = Bcrypt(app)
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'mypostapi')

@app.route('/')
def index():
    all_posts = mysql.query_db("SELECT * FROM posts")
    return render_template('index2.html', all_posts=all_posts)


@app.route('/posts/create', methods=['POST'])
def create():
    session['description'] = request.form['description']
    insert_query = "INSERT INTO `mypostapi`.`posts` (description, created_at, updated_at) VALUES (:description, NOW(), NOW())"
    data = { "description": request.form['description'] }
    mysql.query_db(insert_query, data)
    new_query = "SELECT description FROM posts ORDER BY created_at DESC"
    posts = mysql.query_db(new_query)
    return redirect('/')


app.run(debug=True)
