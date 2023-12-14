use database DEMO1_DB;
use schema PUBLIC;

create table fidelity_test_users1 if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);


create table fidelity_users1 if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);


insert into DEMO1_DB.public.fidelity_test_users1 values('Siddharth','Agarwal','2020-01-01 12:23:23');
