use test;

create table tbl_member(
    email varchar(255) primary key,
    password varchar(255) not null,
    name varchar(255) not null
);

select * from tbl_member;

create table tbl_product(
    id bigint auto_increment primary key,
    name varchar(255) not null,
    price int default 0,
    created_date datetime
);

select * from tbl_product;

