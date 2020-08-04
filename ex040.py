n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média foi {} e você foi REPROVADO'.format(media))
elif 5 <= media <= 6.9:
    print('Sua média foi {} e você está em RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {} e você foi APROVADO!!'.format(media))
