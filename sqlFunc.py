class SqlFunc:

    
    def selectPassword(user_id, password):
        sql = "select * from user_pass WHERE user_id = '%s'  AND password = '%s'" % (user_id, password)
        return sql

    def selectUserList():
        sql = "select * from user_data order by user_id"
        return sql

    def selectKokyakuList():
        sql = "select * from kokyaku_data order by kokyaku_id"
        return sql

    def selectKokyaku(kokyaku_id):
        sql = "select * from kokyaku_data where kokyaku_id = '%s'" % (kokyaku_id)
        return sql

    def selectKokyakuRireki(kokyaku_id):
        sql = '''select kokyakuRireki.* ,menu.menu_nm ,menu.menu_kg 
        from kokyakuRireki inner join menu 
        on kokyakuRireki.menu_id = menu.menu_id
        where kokyaku_id = '%s'
        '''% (kokyaku_id)
        return sql

