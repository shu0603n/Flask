drop table k_rireki;
create table k_rireki (
  kokyaku_id integer
  , start_dt date not null
  , end_dt date not null
  , menu_id integer not null
  , ninzu integer
  , room character varying(10)
  , memo character varying(100)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (kokyaku_id, start_dt)
  , foreign key (kokyaku_id) references k_kihon(kokyaku_id)
);

insert into k_rireki values(1,'2021/01/01'::date,'2021/01/02'::date,1,1,'101','楽しそうだった',null);
insert into k_rireki values(1,'2021/02/01'::date,'2021/02/02'::date,2,2,'101','楽しそうだった',null);
insert into k_rireki values(1,'2021/03/01'::date,'2021/03/02'::date,3,3,'101','楽しそうだった',null);
insert into k_rireki values(1,'2021/04/01'::date,'2021/04/02'::date,4,4,'101','楽しそうだった',null);

insert into k_rireki values(2,'2021/01/01'::date,'2021/01/02'::date,1,1,'101','楽しそうだった',null);
insert into k_rireki values(2,'2021/02/01'::date,'2021/02/02'::date,2,2,'101','楽しそうだった',null);
insert into k_rireki values(2,'2021/03/01'::date,'2021/03/02'::date,3,3,'101','楽しそうだった',null);
insert into k_rireki values(2,'2021/04/01'::date,'2021/04/02'::date,4,4,'101','楽しそうだった',null);

insert into k_rireki values(3,'2021/01/01'::date,'2021/01/02'::date,1,1,'101','楽しそうだった',null);
insert into k_rireki values(3,'2021/02/01'::date,'2021/02/02'::date,2,2,'101','楽しそうだった',null);
insert into k_rireki values(3,'2021/03/01'::date,'2021/03/02'::date,3,3,'101','楽しそうだった',null);
insert into k_rireki values(3,'2021/04/01'::date,'2021/04/02'::date,4,4,'101','楽しそうだった',null);

insert into k_rireki values(4,'2021/01/01'::date,'2021/01/02'::date,1,1,'101','楽しそうだった',null);
insert into k_rireki values(4,'2021/02/01'::date,'2021/02/02'::date,2,2,'101','楽しそうだった',null);
insert into k_rireki values(4,'2021/03/01'::date,'2021/03/02'::date,3,3,'101','楽しそうだった',null);
insert into k_rireki values(4,'2021/04/01'::date,'2021/04/02'::date,4,4,'101','楽しそうだった',null);