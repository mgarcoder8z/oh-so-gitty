from flask import Flask, render_template, request, redirect, make_response, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


@app.route('/')
def index():
    if 'counter' in request.cookies:
        count = int(request.cookies.get('counter')) + 1
        resp = make_response(render_template('index.html', c=count))
        resp.set_cookie('counter', str(count))
    else:
        resp = make_response(render_template('index.html', c=1))
        resp.set_cookie('counter', '1')

    return resp

@app.route('/increment', methods=['post'])
def add_two():
    if 'counter' in request.cookies:
        count = int(request.cookies.get('counter')) + 1
        resp = make_response(redirect('/'))
        resp.set_cookie('counter', str(count))
    else:
        resp = make_response(redirect('/'))
        resp.set_cookie('counter', '2')

    return resp

@app.route('/reset', methods=['post'])
def reset():
    resp = make_response(redirect('/'))
    resp.set_cookie('counter', '0')
    return resp


if __name__ == "__main__":
    app.run(debug=True)
