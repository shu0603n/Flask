drop table p_menu;
create table p_menu (
  menu_id integer not null
  , menu_nm character varying(15) not null
  , menu_kg bigint default 0
  , memo character varying(100)
  , update_dt timestamp default CURRENT_TIMESTAMP
  , primary key (menu_id)
);

insert into p_menu values(1,'のんびりプラン',20000,'のんびりできるプランです',null);
insert into p_menu values(2,'グイグイプラン',20000,'グイグイできるプランです',null);
insert into p_menu values(3,'激安プラン',20000,'激安プランです',null);
insert into p_menu values(4,'高級プラン',20000,'高級プランです',null);