INSERT INTO clientes(nome, cpf, data_nascimento,sexo)
VALUES('roberto','852.741.753-91','2000-10-18','masculino');

INSERT INTO contato_cl(cliente_id,ddd,telefone,email)
VALUES(2,11,985742619,'robertogarvalho@gmail.com');

INSERT INTO enderecos_clientes(cliente_id,rua,numero,bairro,complemento,estado,cidade,cep,referencia)
VALUES(2,'av. mariana',1785,'Mariana','Apartamento','SP','São Paulo',98274-300,'proximo da Casa de ração Joli');

INSERT INTO produtos(nome_produto, precos, quantidade,descrição) 
VALUES ('banco de dados',150,1,'banco de dados para o apartamento');

INSERT INTO pedido(cliente_id,produto_id,statuss,tipo_pgto,qtd_comprada,frete)
VALUES(1,1,'caminho','debíto',1,15);

INSERT INTO material_fornecedor(material,preco_material,quantidade_produto,preco_final,descrição_material)
VALUES('forma para vasos tam 1',6,100,600,'forma de vibra para fazer vaso de pipa baixo tam 1');

INSERT INTO fornecedores(nome_original,nome_fantasia,cnpj,email,mf_id)
VALUES('ceramica tudo em um ltd','tudo em um','25.794.16/0001-40','tudoemum.ceramica@gmail.com.br',2);

INSERT INTO enderecos(fornecedor_id,rua,numero,bairro,complemento,estado,cidade,cep,referencia)
VALUES(2,'R. São marujo',10,'São Vicente','Casa','SP','São Paulo',13528870,'proximo da loja de construção magno');

INSERT INTO contato_fn(fornecedor_id,ddd,telefone,email)
VALUES(2,11,975341882,'tudoemum.ceramica@gmail.com.br');
