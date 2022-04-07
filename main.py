from flask import Flask,request
from flask import render_template
import sqlalchemy as sa
from sqlalchemy.sql import text
import psycopg2

dbUsers = 'postgres'
dbNames = 'PGLOCAL'
dbPassword = 'postgres'
#conn = psycopg2.connect(" user=" + dbUsers +" dbname=" + dbNames +" password=" + dbPassword)
# conn = psycopg2.connect(" dbname=" + dbNames +" password=" + dbPassword)
#conn = psycopg2.connect("host=localhost port=9403 dbname=sampledb user=sayamada password=pssword")
#conn = psycopg2.connect("host=localhost port=5432 dbname=PGLOCAL user=sayamada password=postgres")
# cur = conn.cursor()
# cur.execute()

# # SQLの実行
# sql = text("SELECT * FROM u_password WHERE user_id='test'")
# cur.execute(sql)

# # SQLの実行結果を取得
# for r in cur.fetchall():
#     print(r)
# print("終了")


#set FLASK_WNV=development
#set FLASK_APP=main
#export FLASK_ENV=development
#export FLASK_APP=example
#flask run

app = Flask(__name__)
#データベースのURIはデータベース名に合わせて適宜変更する
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/PGLOCAL'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/',methods=["GET", "POST"])
def index():
    #return render_template('login.html',title="Rope", message="test",user_id='user_id')
    user_id = ''
    return render_template('login.html',user_id=user_id)
    if name == 'main':
        app.debug=True
        app.run()

@app.route("/login",methods=["GET", "POST"])
def login():
    print('login処理開始')
    req = request.args
    user_id = request.form.get("user_id")
    password = request.form.get("password")
  
    if user_id==password:
        return render_template('menu.html',user_id=user_id)
    else:
        return render_template('login.html',user_id=user_id)

@app.route("/menu")
def menu():
    user_id='sss'
    return render_template('menu.html',user_id=user_id)

@app.route("/test/<str>")
def test(str):

    return f'変数は→{ str }です'