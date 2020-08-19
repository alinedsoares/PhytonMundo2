compras = float(input('Qual o valor das suas compras? R$: '))
condicao = int(input('Qual será a condição de pagamento? 1 - à vista dinheiro/cheque | 2 - à vista no cartão | 3 - em até 2x no cartão | 4 - em 3x ou mais no cartão :'))

if condicao == 1:
    print('Sua compras no valor de R$ {:.2f} terão o valor final de R$ {:.2f}.'.format (compras, (compras - (compras * 10 / 100) )))
elif condicao == 2:
    print('Sua compras no valor de R$ {:.2f} terão o valor final de R$ {:.2f}.'.format(compras, (compras - (compras * 5 / 100) )))
elif condicao == 3:
    print('Sua compras no valor de R$ {:.2f} terão o valor final de R$ {:.2f}.'.format(compras, compras))
elif condicao == 4:
    parcelas = int(input('Em quantas parcelas? '))
    if parcelas >= 3:
        print('Sua compras no valor de R$ {:.2f} terão o valor final de R$ {:.2f}.'.format(compras, (compras + (compras * 20 / 100) )))
    else:
        print('Sua compras no valor de R$ {:.2f} terão o valor final de R$ {:.2f}.'.format(compras, compras))
else:
    print('Condição inválida')
