from datetime import date

ano_nascimento = int(input('Digite o seu ano de nascimento: '))
sexo = str(input('Qual o seu sexo M/F? ')).upper().strip()
M = 'masculino'
F = 'feminino'

ano_atual = date.today().year

if sexo == 'F':
    print('Você não precisa de alistar porque é do sexo {}!'.format(F))
elif sexo =='M':
    print('Quem nasceu em {} tem {} anos em {} e como você é do sexo {}:'.format(ano_nascimento, (ano_atual - ano_nascimento), ano_atual, M))
    if ((ano_atual - ano_nascimento) == 18):
        print('É hora de se alistar!!')
    elif ((ano_atual - ano_nascimento) > 18):
        print('Já se passaram {} anos da sua data de alistamento!'.format((ano_atual - 18 - ano_nascimento)))
    else:
        print('Ainda faltam {} anos para a sua data de alistamento.'.format((ano_atual - 18 - ano_nascimento) * -1))
else:
    print('Sexo diferente de M ou F')
    