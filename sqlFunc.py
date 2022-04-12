class SqlFunc:

    
    def selectPassword(user_id, password):
        sql = "select * from user_pass WHERE user_id = '%s'  AND password = '%s'" % (user_id, password)
        return sql

    def selectUserList():
        sql = "select * from user_data order by user_id"
        return sql
