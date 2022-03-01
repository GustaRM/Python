import random
import time

r = 'S'
while r == 'S':
    print('''Sua opções:
    [ 0 ] Pedra
    [ 1 ] Papel
    [ 2 ] Tesoura''')

    j = int(input('Sua jogada: '))
    itens = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = random.randint(0, 2)

    time.sleep(0.2)
    print('JO ', end='')
    time.sleep(0.6)
    print('KEN ', end='')
    time.sleep(0.8)
    print('PÔ!!!')
    time.sleep(0.8)

    corWin = '\033[36m'
    corLose = '\033[31m'
    emp = '\033[33m'
    limpo= '\033[m'

    print('~-~'*8)
    print('''Você jogou {}
    Computador jogou {}'''.format(itens[j], itens[pc]))
    print('~-~'*8)

    if pc == 0: #computador jogou Pedra
        if j == 0:
            print('EMPATE!!!')
        elif j == 1:
            print('VOCÊ VENCEU!!!')
        elif j == 2:
            print('VOCE PERDEU!!!')
        else:
            print('Jogada INVÁLIDA!!!')
    elif pc == 1: #computador jogou Papel
        if j == 0:
            print('VOCE PERDEU!!!')
        elif j == 1:
            print('EMPATE!!!')
        elif j == 2:
            print('VOCÊ VENCEU!!!')
        else:
            print('Jogada INVÁLIDA!!!')
    elif pc == 2: #computador jogou Tesoura
        if j == 0:
            print('VOCÊ VENCEU!!!')
        elif j == 1:
            print('VOCE PERDEU!!!')
        elif j == 2:
            print('EMPATE!!!')
        else:
            print('Jogada INVÁLIDA!!!')

    time.sleep(0.2)
    r = input('\nDeseja jogar novamente? [S/N]: ').upper()

