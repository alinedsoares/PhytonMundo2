numero = int(input('Digite um número inteiro: '))
base = int(input('''Digite uma base de conversão: 
1 - binário, 2 - octal ou 3 - hexadecimal: '''))

if base == 1:
    print('O número decimal {} em sua forma binária é {}'.format(base, bin(numero)[2:]))
elif base == 2:
    print('O número decimal {} em sua forma octal é {}'.format(base, oct(numero)[2:]))
elif base == 3:
    print('O número decimal {} em sua forma hexadecimal é {}'.format(base, hex(numero)[:2]))
else:
    print('Opção inválida!!')
