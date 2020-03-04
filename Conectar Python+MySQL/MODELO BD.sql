drop schema OCORRENCIAS;
create database OCORRENCIAS;
use OCORRENCIAS;

create table ocorrencia(
    id_ocorrencia int primary key not null auto_increment,
    datahora varchar(30),
    relatorio varchar(200),
    armas varchar(10)
);
create table endereco(
    id_endereco int primary key not null auto_increment,
    rua varchar(20),
    bairro varchar(20),
    referencia varchar(100),
    id_ocorrencia int,
    foreign key (id_ocorrencia)references ocorrencia(id_ocorrencia)
);

delimiter //
create trigger delet before delete on ocorrencia
for each row
begin
    delete from endereco where id_ocorrencia = old.id_ocorrencia;
end;//


SELECT * from ocorrencia;
SELECT * from endereco;

INSERT INTO ocorrencia(datahora,relatorio,armas) values("123","dsad","asc");

delete from ocorrencia;


SET SQL_SAFE_UPDATES = 0;





