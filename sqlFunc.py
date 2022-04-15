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

    def selectUriage():
        sql = '''
            select
                kokyakuRireki.start_dt
                , menu.menu_kg
                , kokyaku_data.name_m
                , kokyaku_data.name_s
                , menu.menu_nm
                , kokyakuRireki.ninzu 
            from
                kokyakuRireki 
                inner join kokyaku_data 
                    on kokyakuRireki.kokyaku_id = kokyaku_data.kokyaku_id 
                inner join menu 
                    on kokyakuRireki.menu_id = menu.menu_id
        '''
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

    def updateKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id):
        sql = '''
            update kokyaku_data 
            set
                name_m = '%s'
                , name_s = '%s'
                , name_mk = '%s'
                , name_sk = '%s'
                , jusho1 = '%s'
                , jusho2 = '%s'
                , jusho3 = '%s'
                , jusho4 = '%s'
                , yubin = '%s'
                , email = '%s'
                , tel = '%s'
                , tel_mob = '%s'
                , memo = '%s'
            where
                kokyaku_id = '%s'
        '''% (name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id)

        return sql

    def insertKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id):
        sql = '''
            Insert into 
                kokyaku_data 
            values
                (
                '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                )
        '''% (name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id)

        return sql


        

