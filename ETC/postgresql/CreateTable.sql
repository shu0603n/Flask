drop table user_pass;
create table user_pass (
  user_id character varying(10) not null  primary key
  , password character varying(10) not null
);

drop table user_data;
create table user_data (
  user_id character varying(10) not null primary key
  , name_m  character varying(10) not null
  , name_s  character varying(10) not null
  , name_mk  character varying(10) 
  , name_sk  character varying(10) 
  , jusho1  character varying(10) 
  , jusho2  character varying(10) 
  , jusho3  character varying(30) 
  , jusho4  character varying(30) 
  , yubin  character varying(7) 
  , email  character varying(30) 
  , tel  character varying(11)  
  , tel_mob  character varying(11)  
  , memo  character varying(100)  
);

drop table kokyaku_data;
create table kokyaku_data (
  kokyaku_id character varying(10) not null primary key
  , name_m  character varying(10) not null
  , name_s  character varying(10) not null
  , name_mk  character varying(10) 
  , name_sk  character varying(10) 
  , jusho1  character varying(10) 
  , jusho2  character varying(10) 
  , jusho3  character varying(30) 
  , jusho4  character varying(30) 
  , yubin  character varying(7)
  , email  character varying(30) 
  , tel  character varying(11)  
  , tel_mob  character varying(11)  
  , memo  character varying(100)  
);