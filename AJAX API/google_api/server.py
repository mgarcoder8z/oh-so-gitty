from flask import Flask, render_template, request, redirect, jsonify
import requests # pip install requests
import urllib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/main/get_locations', methods=['POST'])
def get_location():
    origin = str(request.form['origin'])
    destination = str(request.form['destination'])
        # package the post data from our form into a dictionary
    data = {'origin':origin, 'destination':destination}
        # we then use the urlencode function to format our data to be passed through a query string
        # to the google maps api
    api_key = "AIzaSyCcmCNKyJvdobuF0LHZ6hClxbILlne-l3Y"
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + urllib.urlencode(data) + "&key=" + api_key
    response = requests.get(url).content
    print url, urllib.urlencode(data)
    return response

app.run(debug=True)
