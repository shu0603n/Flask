create table user_pass (
  index integer not null primary key
  , user_id character varying(10) not null
  , password character varying(10) not null
  , primary key (index, user_id, password)
);

create table user (
  index integer not null primary key
  , user_id character varying(10) not null
  , password character varying(10) not null
  , primary key (index, user_id, password)
);

create table kokyaku (
  index integer not null
  , name character varying(15)
  , name_k character varying(15)
  , seinen_dt date
  , jusho1 character varying(100)
  , jusho2 character varying(100)
  , primary key (no)
);