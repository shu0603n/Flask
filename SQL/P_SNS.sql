drop table p_sns;
create table p_sns (
  sns_id integer
  , sns_nm character varying(30)
  , url character varying(100)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (sns_id)
);

insert into p_sns values(1,'Twitter',null,null);
insert into p_sns values(2,'Instagram',null,null);
insert into p_sns values(3,'LINE',null,null);
insert into p_sns values(4,'facebook',null,null);

