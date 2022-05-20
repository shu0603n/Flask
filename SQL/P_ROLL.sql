drop table p_roll;
create table p_roll (
  roll_id integer
  , roll_nm character varying(30)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (roll_id)
);

insert into p_roll values(0,'管理者',null);
insert into p_roll values(1,'社員',null);
insert into p_roll values(2,'アルバイト',null);