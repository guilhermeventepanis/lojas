#  Loja Artesanais #
Lojas de Artesanais é uma loja que tem produtos feito a mão(trabalho manual, não industrializado).
#### **Banco de Dados** ####
Criamos um Banco de Dados para a loja de artesanatos para ajudar no gerenciamento sendo mais preciso, agil e ter uma estrutura de informação organizado, como tambem ter mais informações sobre o estoque(sendo a saida de produtos e chegada), como o preço do produto ou materia que entra na loja(compra) e depois a saída do produto (venda), entre outras ajudas.

## Diagrama ##
Diagrama é importante para fazer um trazer facilidade compreensão da entrutura do banco de dados da loja de artesanato antes da criação do banco de dados, seria uma representação graficas de toda a loja sendo representado como entidade (a palavra mais importante podendo ser o sala de aula), atributo (parte ligada a entidade podendo ser aluno, professor, etc.) e relacionamento (que liga duas entidade), entre outras.

<div align="center">
<img src="https://github.com/guilhermeventepanis/lojas/blob/main/Diagrama%20loja%20artesanais%20final-diagrama%20l.%20artesanato.jpg"width ="550px" />
</div>

## Modelo Físico do Bando de Dados ##
Iremos usar o progrma MySQL fazendo a criação das tabelas, inserção de dados e consultas das tabelas do banco de dados, sendo gerenciado os dados obitidos, lembrando que é uma linguagem de programação voltada tambem ao banco de dados.

<div align="center">
<img src="https://github.com/guilhermeventepanis/lojas/blob/main/Diagrama%20loja%20artesanais%20final-diagrama%20l.%20artesanato.jpg"width ="550px" />
</div>

### Código SQL
##### demonstração da criação da tabela de cliente
create table clientes(
cliente_id int primary key not null auto_increment,
nome varchar(255) not null,
cpf varchar(14) not null,
data_nascimento date not null,
sexo varchar(12) not null);

#### Código criação das tabelas SQL
[aberte aqui](https://github.com/guilhermeventepanis/lojas/blame/main/tabelas%20criando.sql)

#### Código SQL inserção de alguns dados teste
[aberte aqui](https://github.com/guilhermeventepanis/lojas/blame/main/inclus%C3%A3o%20de%20alguns%20nomes.sql)

#### averiguação dos dados
[aberte aqui](https://github.com/guilhermeventepanis/lojas/blame/main/como%20olhar%20ele.sql)

## *Python* ##
Vinculamos com o Python para ter uma criação de tabelas mais precisa, facilitação do preenchimento das tabelas, podendo colocar privações, mostrando a lista do cadastro mais rapido, sendo uma liguagem de programação mais usada, agil e com uma velocidade de criação mais rapidos do que os outros tipos de progrmação como o Java e C++.
### Código Python
##### pequena demonstração do código
  
              if usuario_p1_a == 1:
                  nome_completo = str(input('digite seu nome completo:'))
                  cpf = str(input('Digite seu CPF com os pontos e traços: '))
                  data_nascimento = str(input('Digite a data de nascimento, sem traço,(aaa-mm-dd): '))
                  sexo = str(input('qual é o seu sexo: '))
                  
                  sql = f"INSERT INTO clientes(nome, cpf, data_nascimento,sexo) VALUES('{nome_completo}','{cpf}','{data_nascimento}','{sexo}')"
                  
                  cursor.execute(sql)
                  
                  con.commit()
##### Vinculando Python com Mysql
para continuar o projeto precisei vincular Mysql,o nosso banco de dados lojas artesanatos, com Python(usei o PyCharm).

[Código para vincular](https://github.com/guilhermeventepanis/lojas/blob/main/BancodeDados%20part2.py)

##### Fazer a interatividade
Fazendo a interatividade com o cliente, funcionario da loja e etc. com o Banco de dados.
podendo utilizar restrições para falso CPF(nesse caso não criei por motivo de memoria), podendo fazer ciclos em alguns lugares para facilitar mais de um cadastro, fazendo botões de ineratividade,etc.

[Código do python](https://github.com/guilhermeventepanis/lojas/blame/main/python%20informacao_bd%20p2.py)


