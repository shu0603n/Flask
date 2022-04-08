from cmath import nan
from flask import Flask,request
from flask import render_template
from pandas import isnull
import psycopg2

#実行方法
#コマンドプロンプトで下記を実行。
"""
set FLASK_APP=app
set FLASK_WNV=development
flask run
"""

app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():
    print('login処理開始')
  
    #DBの接続情報を取得
    con = connect()

    req = request.args
    #画面から送られてきたパラメータを変数に代入
    user_id = request.form.get("user_id")
    password = request.form.get("password")

    #SQL文にバインド変数を代入する。
    sql =  "select * from u_password WHERE user_id = '%s'  AND password = '%s'" % (user_id, password)

    #SQLを実行し戻り値として結果を受け取る
    res = select_execute(con, sql)

    #DB接続を終了
    con.close()

    if len(res) == 0:
        print('パスワードが一致しません')
        message='パスワードが一致しませんでした'
        return render_template('index.html',user_id=user_id,message=message)
    else:
        print('パスワードが一致しました')
        return render_template('menu.html',user_id=user_id)

@app.route("/menu")
def menu():
    user_id='sss'
    return render_template('menu.html',user_id=user_id)

@app.route("/index")
def signin():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/test/<str>")
def test(str):
    return f'変数は→{ str }です'

#DB情報取得
def connect():
    host     = "localhost"
    port     = "5432"
    dbname   = "PGLOCAL"
    user     = "postgres"
    password = "postgres"
    con = psycopg2.connect("host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + password )
    print("DB接続を開始しました")
    return con

#SELECTを実行
def select_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    return rows
#UPDATEを実行
def updatet_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
    con.commit()
#INSERTを実行
def insert_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
    con.commit()
#DELETEを実行
def delete_execute(con, sql):
    with con.cursor() as cur:
        cur.execute(sql)
    con.commit()