# #!/usr/local/bin/python3.4
# # coding: utf-8
# from urllib.parse import urlparse
# import mysql.connector

# #
# # ＤＢアクセス管理クラス
# #
# class dbAccessor:

#     # -----------------------------------
#     # コンストラクタ
#     #
#     # コネクションを取得し、クラス変数にカーソルを保持する。
#     # -----------------------------------
#     def __init__(self, dbName, hostName, id, password):
#         print("start:__init__")

#         # DB接続URLを作成してパース
#         url = 'mysql://' + id + ':' + password + '@' + 
#             hostName + '/' + dbName
#         parse = urlparse(url)

#         try:
#             # DBに接続する
#             self.conn = mysql.connector.connect(
#                 host = parse.hostname,
#                 port = parse.port,
#                 user = parse.username,
#                 password = parse.password,
#                 database = parse.path[1:],
#             )

#             # コネクションの設定
#             self.conn.autocommit = False

#             # カーソル情報をクラス変数に格納
#             self.conn.is_connected()
#             self.cur = self.conn.cursor()
#         except (mysql.connector.errors.ProgrammingError) as e:
#             print(e)

#         print("end:__init__")

#     # -----------------------------------
#     # クエリの実行
#     #
#     # クエリを実行し、取得結果を呼び出し元に通知する。
#     # -----------------------------------
#     def excecuteQuery(self, sql):
#         print("start:excecuteQuery")

#         try:
#             self.cur.execute(sql)
#             rows = self.cur.fetchall()
#             return rows
#         except (mysql.connector.errors.ProgrammingError) as e:
#             print(e)

#         print("end:excecuteQuery")

#     # -----------------------------------
#     # インサートの実行
#     #
#     # インサートを実行する。
#     # -----------------------------------
#     def excecuteInsert(self, sql):
#         print("start:excecuteInsert")

#         try:
#             self.cur.execute(sql)
#             self.conn.commit()
#             return self.cur.rowcount
#         except (mysql.connector.errors.ProgrammingError) as e:
#             self.conn.rollback()
#             print(e)

#         print("end:excecuteInsert")

#     # -----------------------------------
#     # アップデートの実行
#     #
#     # アップデートを実行する。
#     # -----------------------------------
#     def excecuteUpdate(self, sql):
#         print("start:excecuteUpdate")

#         try:
#             self.cur.execute(sql)
#             self.conn.commit()
#             return self.cur.rowcount
#         except (mysql.connector.errors.ProgrammingError) as e:
#             self.conn.rollback()
#             print(e)

#         print("end:excecuteUpdate")

#     # -----------------------------------
#     # デリートの実行
#     #
#     # デリートを実行する。
#     # -----------------------------------
#     def excecuteDelete(self, sql):
#         print("start:excecuteDelete")

#         try:
#             self.cur.execute(sql)
#             self.conn.commit()
#             return self.cur.rowcount
#         except (mysql.connector.errors.ProgrammingError) as e:
#             self.conn.rollback()
#             print(e)

#         print("end:excecuteDelete")

#     # -----------------------------------
#     # デストラクタ
#     #
#     # コネクションを解放する。
#     # -----------------------------------
#     def __del__(self):
#         print("start:__del__")
#         try:
#             self.conn.close()
#         except (mysql.connector.errors.ProgrammingError) as e:
#             print(e)
#         print("end:__del__")