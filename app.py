import os

from flask import Flask, redirect, url_for,\
    render_template, request, session, flash
from datetime import timedelta
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

def allow_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/Project1", methods=['GET', 'POST'])
def Project1():
    return render_template("Project1.html")



if __name__=="__main__":
    app.run(debug=True)