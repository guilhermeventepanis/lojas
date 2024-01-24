import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senai',
    database='lojas_artesanais'
)

if conexao.is_connected(): #verdadeiro se conector
    print('banco conectado com sucesso')
else:
    print('erro conectado com o banco de dados')
