create database prueba;
use prueba;

create table tabla1(
	campo1 varchar(20),
    campo2 varchar(20)
);

insert into tabla1 values('hola','adios');
insert into tabla1 values('prueba1', 'preba 2');
insert into tabla1 values('prueba3', 'preba 4');
insert into tabla1 values('aaaaaaa', 'bbbbbbb');

select * from tabla1;