show databases;
use invdb;
create table Product(
	Name varchar(50) not null,
    Brand varchar(50) not null,
    Color varchar(20) not null,
    ID varchar(10) not null,
    constraint product_pk primary key(ID)
)