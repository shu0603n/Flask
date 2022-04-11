create table user_pass (
  user_id character varying(10) not null  primary key
  , password character varying(10) not null
);

create table user_data (
  user_id character varying(10) not null primary key
  , name_m  character varying(10) not null
  , name_s  character varying(10) not null
  , name_mk  character varying(10) 
  , name_sk  character varying(10) 
  , jusho1  character varying(30) 
  , jusho2  character varying(30) 
  , yubin  numeric 
  , email  character varying(30) 
  , tel  numeric 
  , tel_mob  numeric 
  , memo  numeric 
);

create table kokyaku_data (
  index character varying(10) not null primary key
  , name_m  character varying(10) not null
  , name_s  character varying(10) not null
  , name_mk  character varying(10) 
  , name_sk  character varying(10) 
  , jusho1  character varying(30) 
  , jusho2  character varying(30) 
  , yubin  numeric 
  , email  character varying(30) 
  , tel  numeric 
  , tel_mob  numeric 
  , memo  numeric 
);