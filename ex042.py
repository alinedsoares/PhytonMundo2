reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceita reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As retas acima podem formar um triângulo')
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    if reta1 != reta2 and reta2 != reta3 and reta1!= reta3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas acima não podem formar um triângulo')
