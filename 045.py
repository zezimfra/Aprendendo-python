from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

jogador = int(input('Qual é a sua escolha? '))

if jogador not in [0, 1, 2]:
    print('ESCOLHA \033[34mINVÁLIDA\033[m')
else:

    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA')

    print('-='*11)
    print('O computador jogou {}.'.format(itens[computador]))
    print('O jogador jogou {}.'.format(itens[jogador]))
    print('-='*11)

    if computador == 0:
        if jogador == 0:
            print('\033[33mEMPATE\033[m')
        elif jogador == 1:
            print('JOGADOR \033[32mVENCEU\033[m')
        elif jogador == 2:
            print('COMPUTADOR \033[31mVENCEU\033[m')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR \033[31mVENCEU\033[m')
        elif jogador == 1:
            print('\033[33mEMPATE\033[m')
        elif jogador == 2:
            print('JOGADOR \033[32mVENCEU\033[m')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR \033[32mVENCEU\033[m')
        elif jogador == 1:
            print('COMPUTADOR \033[31mVENCEU\033[m')
        elif jogador == 2:
            print('\033[33mEMPATE\033[m')