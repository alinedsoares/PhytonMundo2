from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento do atleta ? '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('O atleta possui {} anos e sua categoria é:'.format(idade))

if idade <= 9:
	print('MIRIN.')
if idade <= 14:
	print('INFANTIL.')
if idade <= 19:
	print('JUNIOR.')
if idade <= 22:
	print('SÊNIOR.')
else:
	print('MASTER.')
	
	


