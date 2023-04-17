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

@app.route('/updatetrip')
def CalElectic():
    return render_template("EditTrip.html")

@app.route('/tripdetail')
def CalAir():
    return render_template("TripDetail.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081")