from flask import Flask
from flask import render_template

#$env:FLASK_APP = "main"  
#flask run
app = Flask(__name__)

@app.route("/")
def login():
    user_id='sss'
    return render_template('login.html',login_id='user_id')

@app.route("/menu")
def menu():
    return "<p>menu</p>"

@app.route("/test/<str>")
def str(str):
    return "<p>{str}</p>"
    