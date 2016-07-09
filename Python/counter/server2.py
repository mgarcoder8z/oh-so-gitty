from flask import Flask, render_template, request, redirect, make_response, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
app.count = 0

@app.route('/')
def index():
    # Initialise the counter, or increment it
    session['counter'] += 1
    return render_template('index.html', c=count)
app.run(debug=True)
