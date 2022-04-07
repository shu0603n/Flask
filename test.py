from flask import Flask
from flask import render_template

#$env:FLASK_WNV=development
#$env:FLASK_APP=main
#flask run

#set FLASK_WNV=development
#set FLASK_APP=main 
#export FLASK_ENV=development
#export FLASK_APP=example
#flask run

app = Flask(__name__)

#デバッグモードの有効化
#app.run(debug=True)

@app.route("/")
def login():
    user_id='sss'
    return render_template('login.html',login_id='user_id')

@app.route("/menu")
def menu():
    return "<p>menu</p>"

@app.route("/test/<str>")
def test(str):

    return f'変数は→{ str }です'
    
@app.route("/test2/<str2>")
def test2(str2):

    return f'html{ str2 }'

    