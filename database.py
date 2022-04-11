import psycopg2
class DataBase:

    #DB情報取得
    def connect():
# Host
# ec2-34-207-12-160.compute-1.amazonaws.com
# Database
# d360nfch4hl8mt
# User
# ifnxktkdxwankq
# Port
# 5432
# Password
# 07c61dd3a3d8e7e6b73f58038695a8ebb9e994a92d93651abbfe14121e198674
# URI
# postgres://ifnxktkdxwankq:07c61dd3a3d8e7e6b73f58038695a8ebb9e994a92d93651abbfe14121e198674@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d360nfch4hl8mt
# Heroku CLI
# heroku pg:psql postgresql-silhouetted-72488 --app q-sys-tem

        # 本番環境
        host     = "ec2-34-207-12-160.compute-1.amazonaws.com"
        port     = "5432"
        dbname   = "d360nfch4hl8mt"
        user     = "ifnxktkdxwankq"
        password = "07c61dd3a3d8e7e6b73f58038695a8ebb9e994a92d93651abbfe14121e198674"

        # # LOCAL環境
        # host     = "localhost"
        # port     = "5432"
        # dbname   = "PGLOCAL"
        # user     = "postgres"
        # password = "postgres"
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