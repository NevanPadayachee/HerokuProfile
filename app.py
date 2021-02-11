import os

from flask import Flask, redirect, url_for,\
    render_template, request, session, flash
from datetime import timedelta
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/Project1", methods=['GET', 'POST'])
def Project1():
    return render_template("Project1.html")

@app.route("/Project2")
def Project2():
    return render_template("Project2.html")

@app.route("/Project3")
def Project3():
    return render_template("Project3.html")

if __name__=="__main__":
    app.run(debug=True)