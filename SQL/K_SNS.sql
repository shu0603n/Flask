drop table k_sns;
create table k_sns (
  kokyaku_id integer
  , sns_id integer
  , account character varying(30)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (kokyaku_id, sns_id)
  , foreign key (kokyaku_id) references k_kihon(kokyaku_id)
  , foreign key (sns_id) references p_sns(sns_id)
);

insert into k_sns values(1,1,'@aaaa',null);
insert into k_sns values(1,2,'@aaaa',null);
insert into k_sns values(1,3,'@aaaa',null);
insert into k_sns values(1,4,'@aaaa',null);

insert into k_sns values(2,1,'@aaaa',null);
insert into k_sns values(2,2,'@aaaa',null);
insert into k_sns values(2,3,'@aaaa',null);
insert into k_sns values(2,4,'@aaaa',null);