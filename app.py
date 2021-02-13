import os

from flask import Flask, redirect, url_for,\
    render_template, send_file, current_app


UPLOAD_FOLDER = 'static'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/Project1")
def Project1():
    return render_template("Project1.html")


@app.route("/Project2")
def Project2():
    return render_template("Project2.html")


@app.route("/Project3")
def Project3():
    return render_template("Project3.html")


@app.route("/CV")
def cv():
    return render_template("CV.html")


if __name__=="__main__":
    app.run(debug=True)