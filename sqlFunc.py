class SqlFunc:

    
    def selectPassword(user_id, password):
        sql = "select * from u_pass WHERE user_id = '%s'  AND password = '%s'" % (user_id, password)
        return sql

    def selectUserList():
        sql = "select * from u_data order by user_id"
        return sql

    def selectKokyakuList():
        sql = "select * from k_data order by kokyaku_id"
        return sql

    def selectKokyaku(kokyaku_id):
        sql = "select * from k_data where kokyaku_id = '%s'" % (kokyaku_id)
        return sql

    def selectUriage():
        sql = '''
            select
                k_rireki.start_dt
                , menu.menu_kg
                , k_data.name_m
                , k_data.name_s
                , menu.menu_nm
                , k_rireki.ninzu 
            from
                k_rireki 
                inner join k_data 
                    on k_rireki.kokyaku_id = k_data.kokyaku_id 
                inner join menu 
                    on k_rireki.menu_id = menu.menu_id
        '''
        return sql

    def selectKokyakuRireki(kokyaku_id):
        sql = '''
            select
                k_rireki.*
                , menu.menu_nm
                , menu.menu_kg 
            from
                k_rireki 
                inner join menu 
                    on k_rireki.menu_id = menu.menu_id 
            where
                kokyaku_id = '%s'
        '''% (kokyaku_id)
        return sql

    def selectYoyakuList():
        sql = '''
            select
                k_data.kokyaku_id
                , k_data.name_m
                , k_data.name_s
                , k_data.name_mk
                , k_data.name_sk
                , k_rireki.start_dt
                , k_rireki.end_dt 
            from
                k_data 
                inner join k_rireki 
                    on k_data.kokyaku_id = k_rireki.kokyaku_id 
                    and CURRENT_TIMESTAMP between k_rireki.start_dt and k_rireki.end_dt 
        '''

        return sql

    def updateKokyakuData(name_m,name_s,name_mk,name_sk,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,kokyaku_id):
        sql = '''
            update k_data 
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

    def insertKokyakuData(name_m,name_s,name_mk,name_sk,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo):
        sql = '''
            Insert into 
                k_data 
            values
                (
                nextval('kokyaku_seq')
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , 27
                , '2021/02/03'::date
                , '男'
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
        '''% (name_m,name_s,name_mk,name_sk,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo)

        return sql

    def insertKokyakuRireki(kokyaku_id,start_dt,end_dt,menu_id,ninzu):
        sql = '''
            Insert into 
                k_rireki
            values
                (
                %s
                , '%s'::date
                , '%s'::date
                , %s
                , %s
                )
        '''% (kokyaku_id,start_dt,end_dt,menu_id,ninzu)

        return sql

        

