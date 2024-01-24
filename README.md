#  Loja Artesanais #
Lojas de Artesanais é uma loja que tem produto feito a mão (trabalho manual, não industrializado).
#### **Banco de Dados** ####
Criamos um Banco de Dados para a loja de artesanatos para ajudar no gerenciamento sendo mais preciso ágil e ter uma estrutura de informação organizada, como também ter mais informações sobre o estoque (sendo à saída de produtos e chegada), como o preço do produto ou matéria que entra na loja (compra) e depois a saída do produto (venda), entre outras ajudas.

## Diagrama ##
Diagrama é importante para trazer facilidade na compreensão da estrutura do banco de dados da loja de artesanato antes da criação do banco de dados, seria uma representação gráfica de toda a loja sendo representado como entidade (a palavra mais importante podendo ser a sala de aula), atributo (parte ligada a entidade podendo ser aluno, professor, etc.) e relacionamento (ligação de duas entidades), entre outras.

<div align="center">
<img src="https://github.com/guilhermeventepanis/lojas/blob/main/Diagrama%20loja%20artesanais%20final-diagrama%20l.%20artesanato.jpg"width ="550px" />
</div>


### Modelagem de Relacionamento Logico
Modelagem de relacionamento Logico servir para a aplicação de um sistema da empresa, fazendo um mapa mais técnico da empresa com regras.
fundamentais para colher os requisitos de negócio e retratar os requisitos como um modelo.

<div align="center">
<img src="https://github.com/guilhermeventepanis/lojas/blob/main/modelagem%20de%20relacionamento%201%20loja%20artesanais%202-1-relacionamento%20modelagem%20(1).jpg"width ="500px" />
</div>

# Modelagem de Relacionamento Normalizado
Reflete ao banco de dados otimizado, livre de redundâncias e dependência transitiva, preservando a integridade referencial, garantindo a eficiência, atendendo as demandas especificadas.
<div align="center">
<img src="https://github.com/guilhermeventepanis/lojas/blob/main/modelagem%20de%20relacionamento%20part%202%20loja%20artesanais%202.jpg"width ="500px" />
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
Vinculamos com o Python para ter uma criação de tabelas mais precisa, facilitação do preenchimento das tabelas, podendo colocar privações, mostrando a lista do cadastro mais rápido, sendo uma linguagem de programação mais usada, ágil e com uma velocidade de criação mais rápida do que os outros tipos de programação como o Java e C++.
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
Para continuar o projeto precisei vincular Mysql,o nosso banco de dados lojas artesanatos, com Python (usei o PyCharm).

[Código para vincular](https://github.com/guilhermeventepanis/lojas/blob/main/BancodeDados%20part2.py)

##### Fazer a interatividade
Fazendo a interatividade com o cliente, funcionário da loja e etc. com o Banco de dados.
Podendo utilizar restrições para falso CPF (nesse caso não criei por motivo de memoria), podendo fazer ciclos em alguns lugares para facilitar mais de um cadastro, fazendo botões de interatividade, etc.

[Código do python](https://github.com/guilhermeventepanis/lojas/blame/main/python%20informacao_bd%20p2.py)


#### Conclusão do Projeto do Banco de dados da Loja artesanatos
Esse projeto banco de dados me mostrou que tendo um bom banco de dados à porcentagem aumenta de melhorar ou dar certo a empresa, mais também podendo coletar boas informações pode ser útil no futuro como saber qual produto vende mais e qual vende menos, quais vendedores não vendem e qual mais vende, podendo ver qual é a receita final, com todas as vendas – compras, qual produto realmente precisa comprar, etc.
Agradeço ao auxilio do meu professor que dedicou a me ensinar o máximo possível, meus colegas que auxiliou e corrigiu quando precisei e o SENAI que trouxe um bom ambiente, profissionais excelentes e uma boa estrutura.
Estou muito feliz principalmente em conhecer essa área, conhecer novos programas  como o MYSQL, aprender mais de Python e a ferramenta Draw IO, quero continuar dedicando a aprendendo como também ser um profissional melhor e levar meu conhecimento para a futura empresa.
