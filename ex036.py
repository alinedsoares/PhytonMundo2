valor_casa = float(input('Qual o valor do imóvel? R$ '))
salario_comprador = float(input('Qual o valor do seu salário mensal? R$ '))
prazo_anos = int(input('Em quantos anos você pretende pagar o imóvel? '))

prestacao_mensal = valor_casa / (prazo_anos * 12)
limite_prestacao = salario_comprador * 0.30

if prestacao_mensal >= limite_prestacao:
    print('Lamentamos... seu empréstimo foi negado, pois para financiar um imóvel no valor de R${:.2f} a prestação será R${:.2f} que corresponde a mais de 30% do seu salário mensal.'.format(valor_casa, prestacao_mensal))
else:
    print('Parabéns, seu empréstimo foi aprovado e sua prestação mensal será de R$ {:.2f}!'.format(prestacao_mensal))
