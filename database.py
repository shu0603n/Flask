import psycopg2
class DataBase:

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