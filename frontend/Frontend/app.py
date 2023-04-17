import os
from flask import Flask, render_template, send_file, request, send_from_directory
import requests
from pydantic import BaseModel


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("HomePage.html")

@app.route('/addtrip')
def home_path():
    return render_template("AddTrip.html")

@app.route('/updatetrip/<name>')
def editTrip(name):
    return render_template("EditTrip.html", name=name)

@app.route('/tripdetail/<name>')
def detailTrip(name):
    return render_template("TripDetail.html", name=name)

@app.route('/t/<test>')
def test(test):
    return render_template("test.html", test=test)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081")