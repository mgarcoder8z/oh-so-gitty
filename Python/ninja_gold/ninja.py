from flask import Flask, render_template, request, redirect, make_response, session
from datetime import datetime
import os
import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
#random.randrange(0, 101) # random number between 0-100
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process():
    try:
        session['count']
    except KeyError:
        session['count'] = 0

    try:
        session['activities']
    except KeyError:
        session['activities'] = []

    if request.form['building'] == 'farm':
        count = random.randrange(10,21)

    elif request.form['building'] == 'cave':
        count = random.randrange(5,11)

    elif request.form['building'] == 'house':
        count = random.randrange(2,6)

    elif request.form['building'] == 'casino':
        count = random.randrange(-50,51)

    activity = ''
    time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    if count >= 0:
        activity += 'Earned' + ' ' + str(count) + ' ' + 'gold from the' + ' ' + str(request.form['building'])
    else:
        activity += 'Entered a casino and lost' + ' ' + str(count) + ' ' + 'gold ...Ouch...'

    activity += '! ('+ str(time) + ')'
    session['count'] += count
    session['activities'].insert(0,activity)
    return redirect('/')



if __name__ == "__main__":
   app.run(debug=True)
