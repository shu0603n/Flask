drop table k_kihon;
create table k_kihon (
  kokyaku_id integer not null
  , name_m character varying(10) 
  , name_s character varying(10) 
  , name_mk character varying(10)
  , name_sk character varying(10)
  , seinen_dt date
  , age integer
  , gender character varying(3)
  , yubin character varying(7)
  , jusho1 character varying(10)
  , jusho2 character varying(10)
  , jusho3 character varying(30)
  , jusho4 character varying(30)
  , email character varying(30)
  , tel character varying(11)
  , tel_mob character varying(11)
  , memo character varying(100)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (kokyaku_id)
);
select settval('kokyaku_seq',0);
insert into k_kihon values(nextval('kokyaku_seq'),'テスト','テスト','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into k_kihon values(nextval('kokyaku_seq'),'村井','俊介','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into k_kihon values(nextval('kokyaku_seq'),'池田','辰也','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into k_kihon values(nextval('kokyaku_seq'),'高橋','直輝','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);

select * from  k_kihon;
