from flask import Flask,request
from flask import render_template
from pandas import isnull
import database
import sqlFunc

from flask import send_from_directory
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

#SQL接続
"""
heroku pg:psql postgresql-silhouetted-72488 --app q-system-origin
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
#最終動作確認
heroku rollback v38
'''
#heroku更新
'''
git fetch --all
git heroku -avv
'''

app = Flask(__name__)

# @app.route('/favicon.ico')
# def favicon():
#     # return send_from_directory(os.path.join(app.root_path, 'static/img') 
#     return send_from_directory('/', 'static/common') 

    
@app.route('/',methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/login",methods=["GET", "POST"])
def login():

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

    #SQL文にバインド変数を代入する。
    sql = query.selectUriage()
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)

    return render_template('dashboard.html',uriageList=res)

@app.route("/kokyakuList")
def kokyakuList():

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('kokyakuList.html' ,kokyakuList = res)

@app.route("/kokyaku")
def kokyakuIns():
        return render_template('kokyaku.html' ,sum_cnt=0,sum_kg=0)

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
    
    sum_kg = 0
    for i in res2:
        sum_kg += i['menu_kg']

    return render_template('kokyaku.html' ,kokyaku = res[0] ,kokyakuRireki = res2,sum_cnt=len(res2),sum_kg=sum_kg)
    
@app.route("/kokyakuUpdate",methods=["GET", "POST"])
def kokyakuUpdate():
   
    kokyaku_id = request.form.get("kokyaku_id")
    name_m = request.form.get("name_m")
    name_s = request.form.get("name_s")
    name_mk = request.form.get("name_mk")
    name_sk = request.form.get("name_sk")
    tel = request.form.get("tel")
    tel_mob = request.form.get("tel_mob")
    email = request.form.get("email")
    yubin = request.form.get("yubin")
    jusho1 = request.form.get("jusho1")
    jusho2 = request.form.get("jusho2")
    jusho3 = request.form.get("jusho3")
    jusho4 = request.form.get("jusho4")
    memo = request.form.get("memo")

    #変更をコミット
    sql = query.updateKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id)
    db.updatet_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('kokyakuList.html' ,kokyakuList = res)

@app.route("/kokyakuInput",methods=["GET", "POST"])
def kokyakuInput():
    
    return render_template('kokyakuInsert.html')

@app.route("/kokyakuInsert",methods=["GET", "POST"])
def kokyakuInsert():

    print(test)

    kokyaku_id ='nextval(text)'
    name_m = request.form.get("name_m")
    name_s = request.form.get("name_s")
    name_mk = request.form.get("name_mk")
    name_sk = request.form.get("name_sk")
    tel = request.form.get("tel")
    tel_mob = request.form.get("tel_mob")
    email = request.form.get("email")
    yubin = request.form.get("yubin")
    jusho1 = request.form.get("jusho1")
    jusho2 = request.form.get("jusho2")
    jusho3 = request.form.get("jusho3")
    jusho4 = request.form.get("jusho4")
    memo = request.form.get("memo")

    #変更をコミット
    sql = query.insertKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo)
    print(sql)
    db.insert_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('kokyakuList.html' ,kokyakuList = res)

@app.route("/rirekiInsert",methods=["GET", "POST"])
def rirekiInsert():

    print(test)

    kokyaku_id =request.form.get("kokyaku_id")
    start_dt = request.form.get("start_dt")
    end_dt = request.form.get("end_dt")
    menu_id = request.form.get("menu_id")
    ninzu = request.form.get("ninzu")

    menu_id = 1

    #変更をコミット
    sql = query.insertKokyakuRireki(kokyaku_id,start_dt,end_dt,menu_id,ninzu)
    print(sql)
    db.insert_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('kokyakuList.html' ,kokyakuList = res)

@app.route("/yoyaku",methods=["GET", "POST"])
def yoyaku():
    sql = query.selectYoyakuList()
    res = db.select_execute(con, sql)

    for str in res:
        print(str)
    return render_template('yoyaku.html',kokyakuList = res)

@app.route("/uriage",methods=["GET", "POST"])
def uriage():
    #SQL文にバインド変数を代入する。
    sql = query.selectUriage()
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)
    return render_template('uriage.html',uriageList=res)

@app.route("/seisan",methods=["GET", "POST"])
def seisan():
    return render_template('seisan.html')

@app.route("/userList",methods=["GET", "POST"])
def userList():

    #SQLを実行
    sql = query.selectUserList()
    res = db.select_execute(con, sql)

    return render_template('userList.html')
    
@app.route("/user",methods=["GET", "POST"])
def user():
    return render_template('user.html')

@app.route("/userInsert",methods=["GET", "POST"])
def userInsert():
    return render_template('userInsert.html')

@app.route("/menu")
def menu():
    user_id='sss'
    return render_template('dashboard.html',user_id=user_id)

@app.route("/index")
def signin():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('test.html')
