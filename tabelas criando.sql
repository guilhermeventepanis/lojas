create database lojas_artesanais;
use lojas_artesanais;

create table clientes(
cliente_id int primary key not null auto_increment,
nome varchar(255) not null,
cpf varchar(14) not null,
data_nascimento date not null,
sexo varchar(12) not null);

create table contato_cl(
contato_cl_id int primary key not null auto_increment,
cliente_id int,
ddd int not null,
telefone int not null,
email varchar(100) not null,
foreign key (cliente_id) references clientes(cliente_id));

create table enderecos_clientes(
endereco_cliente_id int primary key not null auto_increment,
cliente_id int,
rua varchar(50) not null,
numero int not null,
bairro varchar(30) not null,
complemento varchar(30) not null,
estado varchar(10) not null,
cidade varchar(40) not null,
cep int not null,
referencia varchar(100) not null,
foreign key (cliente_id) references clientes(cliente_id)
);

create table produtos(
produto_id int primary key not null auto_increment,
nome_produto varchar(255) not null,
precos decimal(10,2) not null,
quantidade int not null,
descrição varchar(500) not null
);

create table pedido(
pedido_id int primary key not null auto_increment,
cliente_id int,
produto_id int,
statuss varchar(200) not null,
tipo_pgto varchar(50) not null,
qtd_comprada int not null,
frete decimal(10,2) not null,
foreign key (cliente_id) references clientes(cliente_id),
foreign key (produto_id) references produtos(produto_id));

create table material_fornecedor(
mf_id int primary key not null auto_increment,
material varchar(80) not null,
preco_material decimal(10,2) not null,
quantidade_produto int not null,
preco_final decimal(10,2) not null,
descrição_material varchar(250) not null);

create table fornecedores(
fornecedor_id int primary key not null auto_increment,
nome_original varchar(100) not null,
nome_fantasia varchar(100) not null,
cnpj char(18)not null,
email varchar(100) not null,
mf_id int,
foreign key (mf_id) references material_fornecedor(mf_id));

create table enderecos(
endereco_id int primary key not null auto_increment,
fornecedor_id int,
rua varchar(50) not null,
numero int not null,
bairro varchar(30) not null,
complemento varchar(30) not null,
estado varchar(10) not null,
cidade varchar(40) not null,
cep int not null,
referencia varchar(100) not null,
foreign key (fornecedor_id) references fornecedores(fornecedor_id));

create table contato_fn(
contato_fn_id int primary key not null auto_increment,
fornecedor_id int,
ddd int not null,
telefone int not null,
email varchar(100),
foreign key (fornecedor_id) references fornecedores(fornecedor_id));
