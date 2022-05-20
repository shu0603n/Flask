create table u_kihon (
  user_id character varying(10) not null
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
  , primary key (user_id)
  , foreign key (user_id) references u_password(user_id)
);

insert into p_sns values(1,'Twitter',null,null);

insert into u_kihon values('test','テスト','テスト','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into u_kihon values('murai','村井','俊介','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into u_kihon values('ikeda','池田','辰也','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);
insert into u_kihon values('takahashi','高橋','直輝','ムライ','シュンスケ','1994/06/03'::date,'27','男','0620907','北海道','札幌市','豊平区','1-7-201','shu0603n@gmail.com','0123123456','09095219336','この人はとてもすごい人です',null);

select * from  u_kihon;
