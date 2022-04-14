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
        sql = '''
            select
                kokyakuRireki.*
                , menu.menu_nm
                , menu.menu_kg 
            from
                kokyakuRireki 
                inner join menu 
                    on kokyakuRireki.menu_id = menu.menu_id 
            where
                kokyaku_id = '%s'
        '''% (kokyaku_id)
        return sql

    def selectYoyakuList():
        sql = '''
            select
                kokyaku_data.kokyaku_id
                , kokyaku_data.name_m
                , kokyaku_data.name_s
                , kokyaku_data.name_mk
                , kokyaku_data.name_sk
                , kokyakurireki.start_dt
                , kokyakurireki.end_dt 
            from
                kokyaku_data 
                inner join kokyakurireki 
                    on kokyaku_data.kokyaku_id = kokyakurireki.kokyaku_id 
                    and CURRENT_TIMESTAMP between kokyakurireki.start_dt and kokyakurireki.end_dt 
        '''

        return sql

        

