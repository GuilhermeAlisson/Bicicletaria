totalp = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade: ')
    if idade == 'sair':
        break
    totalp +=1
    if int(idade) <=3:
        ingresso = 0
        print('ingresso custa R$0')
    else:
        if int(idade) >= 12:
            ingresso = 30
            print('ingresso custa R$30')
        else:
            ingresso = 15
            print('ingresso custa R$15')
    dinheiro += ingresso

media = dinheiro / totalp
print('Total de pessoas: {}'.format(totalp))
print('Dinheiro arrecadado: {}'.format(dinheiro))
print('media arrecadada {}'.format(media))