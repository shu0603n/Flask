import psycopg2
import psycopg2.extras

class DataBase:

    #DB情報取得
    def connect():

        # 本番環境
        DATABASE_URL= 'postgres://mnswsarornkacw:7f08440eeee25f91678fa8dd8a651ca466dee35604d472faeebc18469022042f@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d9890aui1o6ucu'
        con = psycopg2.connect(DATABASE_URL)
        # con = psycopg2.connect('postgres://ifnxktkdxwankq:07c61dd3a3d8e7e6b73f58038695a8ebb9e994a92d93651abbfe14121e198674@ec2-34-207-12-160.compute-1.amazonaws.com:5432/d360nfch4hl8mt')
        # LOCAL環境
        # con = psycopg2.connect('host=localhost port=5432 dbname=PGLOCAL user=postgres password=postgres')

        return con

    #SELECTを実行
    def select_execute(con, sql):
        print(sql)
        with con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(sql)
            rows = cur.fetchall()

        return rows
    #UPDATEを実行
    def updatet_execute(con, sql):
        print(sql)
        with con.cursor() as cur:
            cur.execute(sql)
 
        con.commit()
    #INSERTを実行
    def insert_execute(con, sql):
        print(sql)
        with con.cursor() as cur:
            cur.execute(sql)
        con.commit()
    #DELETEを実行
    def delete_execute(con, sql):
        print(sql)
        with con.cursor() as cur:
            cur.execute(sql)
        con.commit()