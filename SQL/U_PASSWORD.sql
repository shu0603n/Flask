drop table u_password;
create table u_password (
  user_id character varying(10) not null
  , password character varying(10) not null
  , roll_id integer not null default 1
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (user_id)
  , foreign key (roll_id) references p_roll(roll_id)
);

insert into u_password values('test','test',0,null);
insert into u_password values('murai','murai',0,null);
insert into u_password values('ikeda','ikeda',1,null);
insert into u_password values('takahashi','takahashi',1,null);
