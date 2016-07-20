from flask import Flask, request, redirect, render_template, session, make_response, flash, jsonify
#from datetime import datetime
import os
import random
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
#bcrypt = Bcrypt(app)
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app,'mynotesapi')

@app.route('/')
def index():
    query = "SELECT * FROM `mynotesapi`.`notes`"
    notes = mysql.query_db(query)
    return render_template('index2.html', notes=notes)

@app.route('/notes/add', methods=['POST'])
def notes_add():
    insert_query = "INSERT INTO `mynotesapi`.`notes` (title, description, created_at, updated_at) VALUES('{}','{}', NOW(), NOW())".format(str(request.form['title']), str(request.form['description']))
    mysql.query_db(insert_query)
    select_query = "SELECT * FROM notes"
    notes = mysql.query_db(select_query)
    return jsonify(notes)

@app.route('/notes/update/<id>', methods=['POST'])
def notes_update(id):
	try:
		update_query = "UPDATE `mynotesapi`.`notes` SET title = :title, description = :description, updated_at = NOW() WHERE id = :id"
		data = {
					'title': str(request.form['title']),
					'description': str(request.form['description']),
					'id': id,
				}
		mysql.query_db(update_query, data)
	except:
		update_query = "UPDATE notes SET description = :description, updated_at = NOW() WHERE id = :id"
		data = {
					'description': str(request.form['description']),
					'id': id,
				}
        mysql.query_db(update_query, data)
        select_query = "SELECT * FROM notes"
        notes = mysql.query_db(select_query, data)
        return jsonify(notes)

@app.route('/notes/delete/<id>', methods=['POST'])
def notes_delete(id):
    	delete_query = "DELETE FROM notes WHERE id = :id"
    	data = { 'id': id }
    	mysql.query_db(delete_query, data)
    	select_query = "SELECT * FROM notes"
    	notes = mysql.query_db(select_query)
        return jsonify(notes)

app.run(debug=True)
