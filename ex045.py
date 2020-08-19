from time import sleep
from random import randint
print(10 * 'GAME ### ')
sleep(1)
print('')
print('Vamos Jogar?')
sleep(2)
opcoes = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''
0- Pedra 
1- Papel
2- Tesoura     
Escolha uma opção : '''))
sleep(1)
print('')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('...')
sleep(1)
print('')

if jogador == 0:
    if computador == 0:
        print('Pedra x Pedra')
        sleep(1)
        print('EMPATE!')
    elif computador == 1:
        print('Pedra x Papel')
        sleep(1)
        print('GANHEI de você!!!')
    else:
        print('Pedra x Tesoura')
        sleep(1)
        print('Você GANHOU!!!')
elif jogador == 1:
    if computador == 0:
        print('Papel x Pedra')
        sleep(1)
        print('Você GANHOU!!!')
    elif computador == 1:
        print('Papel x Papel')
        sleep(1)
        print('EMPATE!')
    else:
        print('Papel x Tesoura')
        sleep(1)
        print('GANHEI de você!!!')
elif jogador == 2:
    if computador == 0:
        print('Tesoura x Pedra')
        sleep(1)
        print('GANHEI de você!!!')
    elif computador == 1:
        print('Tesoura x Papel')
        sleep(1)
        print('Você GANHOU!!!')
    else:
        print('Tesoura x Tesoura')
        sleep(1)
        print('EMPATE!')
else:
    print('Poxa, a opção {} não existe neste jogo :( '.format(jogador))
    sleep(0.5)
    print('Tente novamente...')
