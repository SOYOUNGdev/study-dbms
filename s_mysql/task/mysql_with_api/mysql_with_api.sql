create table tbl_translate(
    id bigint auto_increment primary key,
    text varchar(255) not null
);

select * from tbl_translate;

create table tbl_image(
    id bigint auto_increment primary key,
    file_path varchar(255) default '/upload/',
    file_name varchar(255),
    file_content varchar(255) not null
);

select * from tbl_image;