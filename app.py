from flask import Flask,request,redirect,url_for,session
from datetime import timedelta ,datetime
from flask import render_template
from pandas import isnull
from sqlalchemy import null
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
git add . 
git commit -m 'message'
git push heroku master

git pull heroku master

heroku releases
#最終動作確認
heroku rollback v48

'''
#heroku更新
'''
git pull heroku master
git fetch --all
git heroku -avv
'''

app = Flask(__name__)
# セッションに格納する情報を暗号化
app.secret_key = 'abcdefghijklmn'
# 3分操作がなければセッションを破棄する
app.permanent_session_lifetime = timedelta(minutes=3) 

@app.errorhandler(403)
def page_not_found(error):
    return render_template('pages/error/403.html'), 403
@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages/error/404.html'), 404
@app.errorhandler(500)
def page_not_found(error):
    return render_template('pages/error/500.html'), 500
@app.errorhandler(505)
def page_not_found(error):
    return render_template('pages/error/505.html'), 505
    

@app.route('/',methods=["GET", "POST"])
def index():

    # return render_template('index.html')
    # POSTの場合
    if request.method == "POST":

        #画面から送られてきたパラメータを変数に代入
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        #SQL文にバインド変数を代入する。
        sql = query.selectPassword(user_id, password)
        #SQLを実行し戻り値として結果を受け取る
        res = db.select_execute(con, sql)

        if len(res) != 0:
            #dashboard.htmlに遷移
            session.permanent = True  
            user = request.form.get("id") 
            session["user_id"] = res[0] 
            # session["user_nm"] = res[1] 

            # return redirect(url_for("login"))
        else:
            session.pop('user_id',None)
            session.clear()
        #     #不一致のメッセージをindex.htmlに返す
        #     message='パスワードが一致しませんでした'
        #     return render_template('pages/login.html',user_id=user_id,message=message)

        return redirect(url_for("login"))
   
    else:
        # GETの場合
        if "user_id" in session: 
            return redirect(url_for("login"))

    return render_template("pages/login.html",user_id=null) 

    
@app.route("/login",methods=["GET", "POST"])
def login():

    if "user_id" in session: 
        print("sessionあり")
        return render_template("index.html", user_id=session["user_id"])
    print("sessionなし")
    message='パスワードが一致しませんでした'
    return render_template('pages/login.html',user_id="",message=message)


@app.route("/logout", methods=["GET"])
def logout():
    if "user_id" in session: 
        session.pop('user_id',None)
        session.clear()
        return redirect("/")


@app.route("/dashboard")
def dashboard():

    #SQL文にバインド変数を代入する。
    sql = query.selectUriage()
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)

    return render_template('index.html',uriageList=res)


@app.route("/kokyaku_list")
def kokyaku_list():

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('pages/kokyaku/kokyaku_list.html' ,kokyakuList = res)


@app.route("/kokyaku")
def kokyaku():
    
    return render_template('pages/kokyaku/kokyaku_update.html' ,sum_cnt=0,sum_kg=0)


@app.route("/kokyaku/<kokyaku_id>")
def kokyaku_kokyaku_id(kokyaku_id):
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

    return render_template('pages/kokyaku/kokyaku_update.html' ,kokyaku = res[0] ,kokyakuRireki = res2,sum_cnt=len(res2),sum_kg=sum_kg)


@app.route("/kokyaku_update",methods=["GET", "POST"])
def kokyaku_update():
   
    kokyaku_id  = request.form.get("kokyaku_id")
    name_m      = request.form.get("name_m")
    name_s      = request.form.get("name_s")
    name_mk     = request.form.get("name_mk")
    name_sk     = request.form.get("name_sk")
    tel         = request.form.get("tel")
    tel_mob     = request.form.get("tel_mob")
    email       = request.form.get("email")
    yubin       = request.form.get("yubin")
    jusho1      = request.form.get("jusho1")
    jusho2      = request.form.get("jusho2")
    jusho3      = request.form.get("jusho3")
    jusho4      = request.form.get("jusho4")
    memo        = request.form.get("memo")

    #変更をコミット
    sql = query.updateKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,yubin,jusho2,jusho3,jusho4,email,tel,tel_mob,memo,kokyaku_id)
    db.updatet_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('pages/kokyaku/kokyaku_list.html' ,kokyakuList = res)


@app.route("/kokyaku_input",methods=["GET", "POST"])
def kokyaku_input():
    
    return render_template('pages/kokyaku/kokyaku_input.html')


@app.route("/kokyaku_insert",methods=["GET", "POST"])
def kokyaku_insert():

    kokyaku_id  ='nextval(text)'
    name_m      = request.form.get("name_m")
    name_s      = request.form.get("name_s")
    name_mk     = request.form.get("name_mk")
    name_sk     = request.form.get("name_sk")
    tel         = request.form.get("tel")
    tel_mob     = request.form.get("tel_mob")
    email       = request.form.get("email")
    yubin       = request.form.get("yubin")
    jusho1      = request.form.get("jusho1")
    jusho2      = request.form.get("jusho2")
    jusho3      = request.form.get("jusho3")
    jusho4      = request.form.get("jusho4")
    memo        = request.form.get("memo")

    #変更をコミット
    sql = query.insertKokyakuData(name_m,name_s,name_mk,name_sk,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo)
    print(sql)
    db.insert_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('pages/kokyaku/kokyaku_list.html' ,kokyakuList = res)


@app.route("/kokyaku_rireki_insert",methods=["GET", "POST"])
def kokyaku_rireki_insert():

    kokyaku_id  = request.form.get("kokyaku_id")
    start_dt    = request.form.get("start_dt")
    end_dt      = request.form.get("end_dt")
    # menu_id   = request.form.get("menu_id")
    menu_id     = 1 # 仮
    ninzu       = request.form.get("ninzu")

    #変更をコミット
    sql = query.insertKokyakuRireki(kokyaku_id,start_dt,end_dt,menu_id,ninzu)
    print(sql)
    db.insert_execute(con, sql)

    sql = query.selectKokyakuList()
    res = db.select_execute(con, sql)

    return render_template('pages/kokyaku/kokyaku_list.html' ,kokyakuList = res)


@app.route("/yoyaku",methods=["GET", "POST"])
def yoyaku():
    # sql = query.selectYoyakuList()
    # res = db.select_execute(con, sql)

    # for str in res:
    #     print(str)
    # return render_template('yoyaku.html',kokyakuList = res)
    return render_template('pages/yoyaku/yoyaku_list.html')


@app.route("/uriage_view",methods=["GET", "POST"])
def uriage_view():

    #SQL文にバインド変数を代入する。
    sql = query.selectUriage()
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)
    return render_template('pages/uriage/uriage_view.html',uriageList=res)


@app.route("/uriage_list",methods=["GET", "POST"])
def uriage_list():

    #SQL文にバインド変数を代入する。
    sql = query.selectUriage()
    #SQLを実行し戻り値として結果を受け取る
    res = db.select_execute(con, sql)
    return render_template('pages/uriage/uriage_list.html',uriageList=res)



@app.route("/user_list",methods=["GET", "POST"])
def user_list():

    #SQLを実行
    sql = query.selectUserList()
    res = db.select_execute(con, sql)
    print(res)

    return render_template('pages/user/user_list.html',userList=res)


@app.route("/user/<user_id>")
def user_user_id(user_id):

    print(user_id)

    #SQLを実行
    sql = query.selectUser(user_id)
    res = db.select_execute(con, sql)

    return render_template('pages/user/user_update.html' ,user = res[0] )


@app.route("/user_update",methods=["GET", "POST"])
def user_update():
   
    user_id     = request.form.get("user_id")
    name_m      = request.form.get("name_m")
    name_s      = request.form.get("name_s")
    name_mk     = request.form.get("name_mk")
    name_sk     = request.form.get("name_sk")
    seinen_dt   = datetime.strptime(request.form.get("seinen_dt"), '%Y/%m/%d')
    jusho1      = request.form.get("jusho1")
    jusho2      = request.form.get("jusho2")
    jusho3      = request.form.get("jusho3")
    jusho4      = request.form.get("jusho4")
    yubin       = request.form.get("yubin")
    email       = request.form.get("email")
    tel         = request.form.get("tel")
    tel_mob     = request.form.get("tel_mob")
    memo        = request.form.get("memo")
    

    #変更をコミット
    sql = query.updateUserData(name_m,name_s,name_mk,name_sk,seinen_dt,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,user_id)
    db.updatet_execute(con, sql)

    sql = query.selectUserList()
    res = db.select_execute(con, sql)

    return render_template('pages/user/user_list.html' ,userList = res)


@app.route("/user_input",methods=["GET", "POST"])
def user_input():
    return render_template('pages/user/user_input.html')


@app.route("/user_insert",methods=["GET", "POST"])
def userInsert():

    #SQLを実行
    sql = query.selectUserList()
    res = db.select_execute(con, sql)
    print(res)

    return render_template('pages/user/user_list.html',user = res[0] )

