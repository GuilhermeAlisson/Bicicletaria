#--->variaveis globais abaixo
listaPecas = []
codigoPeca = 0

#--->Inicio de cadastrar_peças
def cadastrarPeca(codigo):
    print('Você Selecionou a Opção de Cadastrar Peça')
    print('Codigo da Peça {}'.format(codigo))
    nome = input('Entre com NOME da peça: ')
    fabricante = input('Entre com FABRICANTE da peça: ')
    valor = int(input('Entre com VALOR(R$) da peça: '))
    dicionarioPeca = {'codigo' : codigo,
                      'nome' : nome,
                      'fabricante' : fabricante,
                      'valor' : valor}
    listaPecas.append(dicionarioPeca.copy()) #--->Copia o dicionario para dentro da lista

#--->Inicio de consultar_pecas
def consultarPeca():
    print('Bem vindo a Consulta de Peças')
    while True:
        opcaoConsultar = input('Escolha a opção desejada: \n'
                               '1 - Consultar Todas as Peças \n'
                               '2 - Consultar Peça por Codigo \n'
                               '3 - Consultar Peças por Fabricante \n'
                               '4 - Retornar \n'
                               '')
        if opcaoConsultar == '1':
            print('Foi escolhido a opção 1 - Consultar Todas as Peças ')
            for pecas in listaPecas: #--->peças vai varrer toda a lista de peças
                print('-' *20)
                for key, value in pecas.items(): #---> varrer todos as chaves e valores do dicionario
                    print('{}: {}'.format(key,value))
                print('-' *20)
        elif opcaoConsultar == '2':
            print('Foi escolhido a opção 2 - Consultar Peças por Codigo')
            codigoDesejado = int(input('Qual codigo desejado: '))
            for pecas in listaPecas:
                if pecas['codigo'] == codigoDesejado: #--->O valor do codigo é igual ao que foi solicitado
                    print('-' * 20)
                    for key, value in pecas.items():  # ---> varrer todos as chaves e valores do dicionario
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
        elif opcaoConsultar == '3':
            print('Foi escolhido a opção 3 - Consultar Peças por Fabricante')
            fabricanteDesejado = input('Qual Fabricante desejado: ')
            for pecas in listaPecas:
                if pecas['fabricante'] == fabricanteDesejado:  # --->O fabricante é igual ao que foi solicitado
                    print('-' * 20)
                    for key, value in pecas.items():  # ---> varrer todos as chaves e valores do dicionario
                        print('{}: {}'.format(key, value))
                    print('-' * 20)
        elif opcaoConsultar == '4':
            print('Foi escolhido a opção 4 - Retornar')
            print('Retornando...')
            return  # --->Sai da função consultarPeca
        else:
            print('Opção invalida! Digite uma opção valida')
            continue  # --->volta para o inicio do while
#--->Inicio de remover_pecas
def removerPeca():
    print('Foi escolhido a opção 4 - Retornar')
    remover = int(input('Coloque o codigo do produto para que seja REMOVIDO: '))
    for pecas in listaPecas:
        if pecas['codigo'] == remover:  # --->O fabricante é igual ao que foi solicitado
            listaPecas.remove(pecas)
            print('Produto Removido')

#--->main
print('Bem vindo ao Controle de Estoque da Bicicletaria do Guilherme Alisson Natalino da Silva')
print('-'*87)
while True:
    opcaoPrincipal = input('Escolha a opção desejada: \n'
                           '1 - Cadastrar peças \n'
                           '2 - Consultar peças \n'
                           '3 - Remover peaças \n'
                           '4 - Sair \n')
    if opcaoPrincipal == '1':
        codigoPeca = codigoPeca +1
        cadastrarPeca(codigoPeca)
    elif opcaoPrincipal == '2':
        consultarPeca()
    elif opcaoPrincipal == '3':
        removerPeca()
    elif opcaoPrincipal == '4':
        print('Saindo...')
        break #--->Sai do programa
    else:
        print('Opção invalida! Digite uma opção valida')
        continue #--->volta para o inicio do while