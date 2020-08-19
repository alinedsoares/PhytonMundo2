peso = float(input('Informe o seu peso (kg): '))
altura = float(input('Informe a sua altura (m): '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f} ' .format(imc))
if imc < 18.5:
    print('e você está abaixo do Peso')
elif 18.5 <= imc < 25:
    print('e você está no Peso Ideal')
elif 25 <= imc < 30:
    print('e você está com Sobrepeso')
elif 30 <= imc < 40:
        print('e você está com Obesidade')
else:
    print('e você está com Obesidade Mórbida')
