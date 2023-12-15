use database DEMO1_DB;
use schema PUBLIC;

create table sid_test_users if not exists(
  name varchar (100),  -- variable string column
  preferences string, -- column used to store JSON type of data
  created_at timestamp
);

insert into DEMO1_DB.public.fidelity_test_users values('payal','jindal','2020-01-01 12:23:23');
