n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('- O primeiro valor é maior do que o segundo.')
elif n2 > n1:
    print('- O segundo valor é maior do que o primeiro.')
else:
    print('- Não existe valor maior, os dois valores são iguais!')
