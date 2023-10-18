import math

print('Bem vindo a Companhia de Logistica do Guilherme Alisson Natalino da Silva')
print('-'*73)

pessoas = 0
while True:
    ingresso = float(input('Entre com o valor total dos ingressos:'))
    pessoas = int(input('Entre com a quantidade de pessoas:'))
    calc = ingresso*pessoas
    if pessoas >=4:
        calcular = math.ceil(pessoas/4)
        print('Número de cadeiras necessarias é de: {}'.format(pessoas))
        print('Número de mesas necessarias de: {}'.format(calcular))
    elif pessoas <=3:
        print('Numero de pessoas insuficente para encher uma mesa, será necessario apenas de uma mesa')
        print('Numero de cadeiras necessarias é de: {}'.format(pessoas))
    else: #--->Verifica se o usuario digitou um numero ou um valor invalido
        print('Você digitou alguma dimensão do objeto com valor não numérico')
    valortotal = calc
    print(f'A quantidade final de valor arrecadado com os ingressos é: R${valortotal:,.2f}'.replace(',','.'))

    continuar = input('Deseja continuar seu planejamento? \n1 - Sim \n0 - Não \n')
    continuar = continuar.upper()  # --->Deixa tudo maiusculo ex: 's' = 'S'
    if continuar == 'S' or continuar == '1':  # ---> Continue com 'S' ou 's' ou '1'
        continue  # --->Continua o programa se for digitado 'S' ou 's'
    else:
        print('Obrigado por confiar na nossa Companhia 🚚'.format(pessoas))
        break

