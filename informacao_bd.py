import BancodeDados

con = BancodeDados.conexao
cursor = con.cursor()

while True:

    print('''
    [1] cadastrar
    [2] listar
    [3] alterar
    [4] deletar 
    [5] sair
    ''')
    usuario_p1 = float(input('qual das opções acima: '))
    if usuario_p1 == 1:
        while True:
            print('''deseja cadastrar o que?        
            [1] Cliente 
            [2] produto
            [3] pedido
            [4] fornecedor
            [5] sair
            ''')
            usuario_p1_a = int(input('Digite uma opção acima: '))
            if usuario_p1_a == 1:
                nome_completo = str(input('digite seu nome completo:'))
                cpf = str(input('Digite seu CPF com os pontos e traços: '))
                data_nascimento = str(input('Digite a data de nascimento, sem traço,(aaa-mm-dd): '))
                sexo = str(input('qual é o seu sexo: '))
                sql = f"INSERT INTO clientes(nome, cpf, data_nascimento,sexo) VALUES('{nome_completo}','{cpf}','{data_nascimento}','{sexo}')"
                cursor.execute(sql)
                con.commit()
                #parte dois do cliente
                print('cadastro endereço: ')
                sql_dois_pum = "SELECT * FROM clientes;"
                cursor.execute(sql_dois_pum)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                cliente_id = int(input('Código do cliente: '))
                rua = str(input('digite o nome da sua rua: '))
                numero = int(input('numero da casa: '))
                bairro = str(input('bairro: '))
                complemento = str(input('complemento(casa,apartamento,etc): '))
                estado = str(input('estado: '))
                cidade = str(input('cidade:'))
                cep = int(input('cep,sem traço e ponto: '))
                referencia = str(input('referencia do lugar: '))
                sql_um_dois = f"INSERT INTO enderecos_cliente(cliente_id,rua,numero,bairro,complemento,estado,cidade,cep,referencia) VALUES('{cliente_id}','{rua}','{numero}','{bairro}','{complemento}','{estado}','{cidade}','{cep}','{referencia}')"
                cursor.execute(sql_um_dois)
                con.commit()
                # parte tres contato_cl
                print('Cadastro do Telefone')
                sql_dois_pum = "SELECT * FROM clientes;"
                cursor.execute(sql_dois_pum)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                cliente_id = int(input('Digite o ID do Cliente: '))
                ddd = int(input('Digite o DDD: '))
                telefone = int(input('Digite o numero de telefone: '))
                email = str(input('Digite seu e-mail: '))
                sql_um_tres = f"INSERT INTO contato_cl(cliente_id,ddd,telefone,e_mail) VALUES('{cliente_id}','{ddd}','{telefone}','{email}')"
                cursor.execute(sql_um_tres)
                con.commit()

            elif usuario_p1_a == 2:
                nome_produto = str(input('Digite o nome do produto: '))
                preco = float(input('Digite o preço do produto, com ponto na casas decimais: R$'))
                quantidade = int(input('qual seria a quantidade da mercadoria: '))
                descricao = str(input('Digite uma preve descrição do produto: '))
                sql_dois = f"INSERT INTO produtos(nome_produto, preco, quantidade,descrição) VALUES ('{nome_produto}','{preco}','{quantidade}','{descricao}')"
                cursor.execute(sql_dois)
                con.commit()

            # Pedido
            elif usuario_p1_a == 3:
                sql_tres_um = "SELECT * FROM clientes;"
                cursor.execute(sql_tres_um)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                cliente_id = int(input('cliente ID: '))
                sql_tres_dois = "SELECT * FROM produtos;"
                cursor.execute(sql_tres_dois)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                produto_id = int(input('digite o ID do Produto: '))
                statuss = str(input('Statuss do produto: '))
                tipo_pgto = str(input('tipo de pagamento: '))
                qtd_comprada = int(input('quantidade comprada: '))
                if qtd_comprada >= 5:
                    km = float(input('digite o km de entrega: '))
                    frete = (km * 0.15) + (5 * 0.10)
                    sql_tres_zero = f"INSERT INTO pedidos(cliente_id, produto_id, statuss, tipo_pgto, qtd_comprada, frete) VALUES('{cliente_id}','{produto_id}','{statuss}','{tipo_pgto}','{qtd_comprada}','{frete}')"
                    cursor.execute(sql_tres_zero)
                    con.commit()
                if qtd_comprada < 5:
                    km = float(input('digite o km de entrega: '))
                    frete = km * (0.15)  # são 15 porcento
                    sql_tres_um = f"INSERT INTO pedidos(cliente_id,produto_id,statuss,tipo_pgto,qtd_comprada,frete) VALUES('{cliente_id}','{produto_id}','{statuss}','{tipo_pgto}','{qtd_comprada}','{frete}')"
                    cursor.execute(sql_tres_um)
                    con.commit()
            #fornecedor
            elif usuario_p1_a == 4:
                material = str(input('Digite o nome do produto: '))
                preco_material = float(input('Qual é o Preço Unitário, com ponto na casas decimais: R$'))
                quantidade_produto = int(input('Qual é a quantidade de produto: '))
                preco_final = preco_material * quantidade_produto
                descricao_material = str(input('qual é a descrição do material: '))
                sql_quatro = (f"INSERT INTO material_fornecedor(material,preco_material,quantidade_produto,preco_final,descrição_material) VALUES('{material}','{preco_material}','{quantidade_produto}','{preco_final}','{descricao_material}')")
                cursor.execute(sql_quatro)
                con.commit()
                #parte 2 do banco de dados
                sql_dois_pum = "SELECT * FROM material_fornecedor;"
                cursor.execute(sql_dois_pum)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                print('vamor para a empresa agora: ')
                mf_id = int(input('informe o código do produto: '))
                nome_original = str(input('Nome de criação da empresa: '))
                nome_fantasia = str(input('Nome fantasia da empresa: '))
                cnpj = str(input('Seu CNPJ, com pontos e traços: '))
                e_mail = str(input('seu e-mail: '))
                sql_quatro_pdois = (f"INSERT INTO fornecedores(nome_original,nome_fantasia,cnpj,e_mail,mf_id) VALUES('{nome_original}','{nome_fantasia}','{cnpj}','{e_mail}','{mf_id}')")
                cursor.execute(sql_quatro_pdois)
                con.commit()
                #parte 3 endereço
                sql_dois_ptres = "SELECT * FROM fornecedores;"
                cursor.execute(sql_dois_ptres)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                print('Endereço do estabelecimento:')
                fornecedor_id = int(input('Qual é o Código do fornecedor: '))
                rua = str(input('Qual é o nome da Rua: '))
                numero = int(input('Qual é o numero: '))
                bairro = str(input('Bairro: '))
                complemento = str(input('Complemento: '))
                estado = str(input('Estado: '))
                cidade = str(input('Cidade: '))
                cep = str(input('CEP, com 8 digitos, sem o traço no final:'))
                sql_quatro_ptres = (f"INSERT INTO enderecos(rua, numero, bairro, complemento, estado, cidade, cep, fornecedor_id) VALUES('{rua}','{numero}','{bairro}','{complemento}','{estado}','{cidade}','{cep}','{fornecedor_id}')")
                cursor.execute(sql_quatro_ptres)
                con.commit()
                #parte 4 contato
                sql_dois_ptres = "SELECT * FROM fornecedores;"
                cursor.execute(sql_dois_ptres)
                retorno_do_banco = cursor.fetchall()
                for i in retorno_do_banco:
                    print("-" * 50)
                    print(i[0], "|", i[1])
                fornecedor_id = int(input('Codigo do fornecedor: '))
                ddd = int(input('Digite seu DDD: '))
                telefone = int(input('seu telefone: '))
            elif usuario_p1_a ==5:
                print('Finalização dos cadastro')
                break
            else:
                print('numero invalido, tente novamente')

    # listando as tabelas
    elif usuario_p1 == 2:
        while True:
            print('''
            [1] cliente
            [2] produto
            [3] pedido
            [4] fornecedor
            [5] Voltar
            ''')
            opcao_list = int(input('digite uma das opções acima: '))
            if opcao_list == 1:
                #cliente
                print('''
                [1] lista todos os clientes
                [2] lista um cliente''')
                opcao = int(input('qual das opções acima: '))
                if opcao == 1:
                    sql_dois_pum= "SELECT * FROM clientes;"
                    cursor.execute(sql_dois_pum)
                    retorno_do_banco = cursor.fetchall()
                    for i in retorno_do_banco:
                        print("-"*50)
                        print(i[0],"|",i[1],"|",i[2],"|",i[3].strftime("%d-%m-%Y"))
                elif opcao == 2:
                    codigo = int(input('informe o código do cliente: '))
                    sql = f"SELECT * FROM clientes where cliente_id = {codigo};"
                    cursor.execute(sql)
                    cliente = cursor.fetchone()
                    print(cliente)
                else:
                    print('opção invalida, tente novamente')

            elif opcao_list == 2:
                #Produto
                print('''
                [1] lista todos os produtos
                [2] lista um produto''')
                opcao = int(input('qual das opções acima: '))
                if opcao == 1:
                    sql_dois_pum= "SELECT * FROM produtos;"
                    cursor.execute(sql_dois_pum)
                    retorno_do_banco = cursor.fetchall()
                    for i in retorno_do_banco:
                        print("-"*50)
                        print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4])
                elif opcao == 2:
                    codigo = int(input('informe o código do cliente: '))
                    sql = f"SELECT * FROM produtos where produto_id = {codigo};"
                    cursor.execute(sql)
                    produto = cursor.fetchone()
                    print(produto)
                else:
                    print('opção invalida, tente novamente')

            elif opcao_list == 3: #pedido
                print('''
                [1] lista todos os Pedidos
                [2] lista um Pedido''')
                opcao = int(input('qual das opções acima: '))
                if opcao == 1:
                    sql_dois_ptres= "SELECT * FROM pedidos;"
                    cursor.execute(sql_dois_ptres)
                    retorno_do_banco = cursor.fetchall()
                    for i in retorno_do_banco:
                        print("-"*50)
                        print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6])
                elif opcao == 2:
                    codigo = int(input('informe o código do pedido: '))
                    sql = f"SELECT * FROM pedidos where pedido_id = {codigo};"
                    cursor.execute(sql)
                    pedido = cursor.fetchone()
                    print(pedido)
                else:
                    print('opção invalida, tente novamente')
            elif opcao_list == 4: #fornecedor
                print('''
                [1] lista todos os fornecedores
                [2] lista um fornecedor''')
                opcao = int(input('qual das opções acima: '))
                if opcao == 1:
                    sql_dois_pquatro= "SELECT * FROM fornecedores;"
                    cursor.execute(sql_dois_pquatro)
                    retorno_do_banco = cursor.fetchall()
                    for i in retorno_do_banco:
                        print("-"*50)
                        print(i[0],"|",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5])
                elif opcao == 2:
                    codigo = int(input('informe o código do pedido: '))
                    sql = f"SELECT * FROM fornecedores where fornecedor_id = {codigo};"
                    cursor.execute(sql)
                    fornecedor = cursor.fetchone()
                    print(fornecedor)

            elif opcao_list == 5:
                print('Listado com Sucesso, Voltando')
                break
            else:
                print('Numero Invalido, tente novamente!!')

    elif usuario_p1 ==3:
        codigo = int(input("informe o codigo do cliente"))
        nome_completo = input('digite o nome novamente: ')
        cpf = str(input('digite seu CPF novamente'))
        data_nascimento = input('digite a data de nascimento (aaaa-mm-dd): ')
        sexo = str(input('qual é o seu sexo: '))
        sql = f'UPDATE clientes SET nome= "{nome_completo}", cpf = "{cpf}", data_nascimento="{data_nascimento}", sexo="{sexo}" '
        cursor.execute(sql)
        con.commit()
        print('cliente atualizado com sucesso! ')

    elif usuario_p1 ==4:
        print('''
        [1]Fornecedor
        [2]Cliente''')
        opcao = int(input('digite a opcao acima: '))
        if opcao == 1:
            sql_quatro_pum = "SELECT * FROM contato_fn;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do contato_fn: '))
            sql_quatro = f"DELETE FROM contato_fn WHERE contato_fn_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            ''''''
            sql_quatro_pum = "SELECT * FROM enderecos;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do enderecos_id: '))
            sql_quatro = f"DELETE FROM enderecos WHERE enderecos_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            sql_quatro_pum = "SELECT * FROM fornecedores;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do fornecedor_id: '))
            sql_quatro = f"DELETE FROM fornecedores WHERE fornecedor_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            print('Fornecedor deletado com sucesso')

        if opcao == 2:
            sql_quatro_pum = "SELECT * FROM pedidos;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do pedido: '))
            sql_quatro = f"DELETE FROM pedidos WHERE pedido_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            sql_quatro_pum = "SELECT * FROM contato_cl;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do contato_cl_id: '))
            sql_quatro = f"DELETE FROM contato_cl WHERE contato_cl_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            sql_quatro_pum = "SELECT * FROM enderecos_cliente;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do endereco cliente: '))
            sql_quatro = f"DELETE FROM enderecos_cliente WHERE endereco_cliente_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
            sql_quatro_pum = "SELECT * FROM clientes;"
            cursor.execute(sql_quatro_pum)
            retorno_do_banco = cursor.fetchall()
            for i in retorno_do_banco:
                print("-" * 50)
                print(i[0], "|", i[1])
            codigo = int(input('qual é o codigo que vai deletar do cliente_id: '))
            sql_quatro = f"DELETE FROM clientes WHERE cliente_id = {codigo};"
            cursor.execute(sql_quatro)
            con.commit()
        else:
            print('opção invalida, tente novamente')
    elif usuario_p1 == 5:
        print('finalizado')
        break
    else:
        print('Numero invalido, Tente novamente')
        continue
