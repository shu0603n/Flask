class SqlFunc:

    
    def selectPassword(user_id, password):
        sql = '''
            select 
                u_pass.user_id 
                , concat(u_kihon.name_m,' ',u_kihon.name_s) as user_nm 
            from u_pass 
            left join u_kihon
                on u_pass.user_id = u_kihon.user_id 
            where 
                u_pass.user_id = '%s' and u_pass.password = '%s'
        ''' % (user_id, password)
        return sql

    def selectUserList():
        sql = "select * from u_kihon order by user_id"
        return sql

    def selectUser(user_id):
        sql = '''
            select 
                u_kihon.* 
                , u_pass,password 
            from u_kihon 
            inner join 
                u_pass on u_kihon.user_id = u_pass.user_id 
            where u_kihon.user_id = '%s'
        ''' % (user_id)
        return sql

    def selectKokyakuList():
        sql = "select * from k_kihon order by kokyaku_id"
        return sql

    def selectKokyaku(kokyaku_id):
        sql = "select * from k_kihon where kokyaku_id = '%s'" % (kokyaku_id)
        return sql
    
    def selectSns(kokyaku_id):
        sql = '''
            select
                k_sns.kokyaku_id
                , k_sns.sns_id
                , p_sns.sns_nm
                , k_sns.account 
            from
                k_sns 
                inner join p_sns 
                    on k_sns.sns_id = p_sns.sns_id
            where
                k_sns.kokyaku_id = '%s'
        '''% (kokyaku_id)
        return sql

    def selectUriage():
        sql = '''
            select
                k_rireki.start_dt
                , p_menu.menu_kg
                , k_kihon.name_m
                , k_kihon.name_s
                , p_menu.menu_nm
                , k_rireki.ninzu 
            from
                k_rireki 
                inner join k_kihon 
                    on k_rireki.kokyaku_id = k_kihon.kokyaku_id 
                inner join p_menu 
                    on k_rireki.menu_id = p_menu.menu_id
        '''
        return sql

    def selectKokyakuRireki(kokyaku_id):
        sql = '''
            select
                k_rireki.*
                , p_menu.menu_nm
                , p_menu.menu_kg 
            from
                k_rireki 
                inner join p_menu 
                    on k_rireki.menu_id = p_menu.menu_id 
            where
                kokyaku_id = '%s'
        '''% (kokyaku_id)
        return sql

    def selectYoyakuList():
        sql = '''
            select
                k_kihon.kokyaku_id
                , k_kihon.name_m
                , k_kihon.name_s
                , k_kihon.name_mk
                , k_kihon.name_sk
                , k_rireki.start_dt
                , k_rireki.end_dt 
            from
                k_kihon 
                inner join k_rireki 
                    on k_kihon.kokyaku_id = k_rireki.kokyaku_id 
                    and CURRENT_TIMESTAMP between k_rireki.start_dt and k_rireki.end_dt 
        '''

        return sql

    def updateKokyakuData(name_m,name_s,name_mk,name_sk,seinen_dt,age,gender,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo,kokyaku_id):
        sql = '''
            update k_kihon 
            set
                name_m = '%s'
                , name_s = '%s'
                , name_mk = '%s'
                , name_sk = '%s'
                , seinen_dt = '%s'::date
                , age = '%s'
                , gender = '%s'
                , yubin = '%s'
                , jusho1 = '%s'
                , jusho2 = '%s'
                , jusho3 = '%s'
                , jusho4 = '%s'
                , email = '%s'
                , tel = '%s'
                , tel_mob = '%s'
                , memo = '%s'
            where
                kokyaku_id = '%s'
        '''% (name_m,name_s,name_mk,name_sk,seinen_dt,age,gender,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo,kokyaku_id)

        return sql

    def insertKokyakuData(name_m,name_s,name_mk,name_sk,seinen_dt,age,gender,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo):
        sql = '''
            Insert into 
                k_kihon 
            values
                (
                nextval('kokyaku_seq')
                , '%s'
                , '%s'
                , '%s'
                , '%s'
                , '%s'::date
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
        '''% (name_m,name_s,name_mk,name_sk,seinen_dt,age,gender,yubin,jusho1,jusho2,jusho3,jusho4,email,tel,tel_mob,memo)

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

    def updateUserData(name_m,name_s,name_mk,name_sk,seinen_dt,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,user_id):
        sql = '''
            update u_kihon 
            set
                name_m = '%s'
                , name_s = '%s'
                , name_mk = '%s'
                , name_sk = '%s'
                , seinen_dt = '%s'::date
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
                user_id = '%s'
        '''% (name_m,name_s,name_mk,name_sk,seinen_dt,jusho1,jusho2,jusho3,jusho4,yubin,email,tel,tel_mob,memo,user_id)

        return sql



        

