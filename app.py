from flask import Flask,request
from flask import render_template
from pandas import isnull
import database
import sqlFunc
#クラスインスタンス化
db = database.DataBase
query =sqlFunc.SqlFunc
#DBの接続情報を取得
con = db.connect()

#実行方法
#コマンドプロンプトで下記を実行。
"""
set FLASK_APP=app
set FLASK_ENV=development
flask run
"""

#停止方法
"""
[Ctrl + C]で停止
再度flask runで起動
"""

#SQL接続
"""
heroku pg：psql postgresql-silhouetted-72488 --app q-system-origin
"""

#Gitデプロイ方法
'''
git add . 
git commit -m 'message'
git push origin master
'''

#herokuデプロイ方法
'''
git pull heroku master
git add . 
git commit -m 'message'
git push heroku master

heroku releases
$ heroku rollback v23
'''
#heroku更新
'''
git fetch --all
git heroku -avv
'''


app = Flask(__name__)


@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():

    print('login処理開始')

    #画面から送られてきたパラメータを変数に代入
    user_id = request.form.get("user_id")
    password = request.form.get("password")

    #SQL文にバインド変数を代入する。
    sql = query.selectPassword(user_id, password)
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)

    if len(res) == 0:
        #不一致のメッセージをindex.htmlに返す
        message='パスワードが一致しませんでした'
        return render_template('index.html',user_id=user_id,message=message)
    else:
        #dashboard.htmlに遷移
        return render_template('dashboard.html',user_id=user_id)

@app.route("/dashboard")
def dashboard():

    return render_template('dashboard.html')

@app.route("/kokyakuList")
def kokyakuList():


    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    for str in res:
        print(str)
        
    return render_template('kokyakuList.html' ,kokyakuList = res)

@app.route("/kokyaku/<kokyaku_id>")
def kokyaku(kokyaku_id):
    print(kokyaku_id)

    #SQLを実行
    sql = query.selectKokyaku(kokyaku_id)
    res = db.select_execute(con, sql)

    #SQLを実行
    sql2 = query.selectKokyakuRireki(kokyaku_id)
    res2 = db.select_execute(con, sql2)
    print(res2)
    
    sum_cnt = len(res2)
    sum_kg = 0
    for i in res2:
        sum_kg += i['menu_kg']
    print(sum_kg)

    return render_template('kokyaku.html' ,kokyaku = res[0] ,kokyakuRireki = res2,sum_cnt=sum_cnt,sum_kg=sum_kg)

@app.route("/kokyakuInsert")
def kokyakuInsert():
    return render_template('kokyakuInsert.html')

@app.route("/yoyaku")
def yoyaku():
    return render_template('yoyaku.html')

@app.route("/uriage")
def uriage():
    return render_template('uriage.html')

@app.route("/seisan")
def seisan():
    return render_template('seisan.html')

@app.route("/userList")
def userList():

    #SQLを実行
    sql = query.selectUserList()
    res = db.select_execute(con, sql)

    return render_template('userList.html')
    
@app.route("/user")
def user():
    return render_template('user.html')

@app.route("/userInsert")
def userInsert():
    return render_template('userInsert.html')

@app.route("/menu")
def menu():
    user_id='sss'
    return render_template('dashboard.html',user_id=user_id)

@app.route("/index")
def signin():
    return render_template('index.html')

@app.route("/test/<str>")
def test(str):
    return f'変数は→{ str }です'
