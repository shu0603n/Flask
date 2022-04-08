class DataBase:
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