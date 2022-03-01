from random import randint

totwin = 0
print('=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)

while True:
    j = int(input('Escolha um número: '))
    pc = randint(0, 11)
    total = j + pc
    parImpar = str(input('Deseja PAR ou ÍMPAR?[P/I]: ').upper())

    while parImpar not in 'PI':
        parImpar = str(input('Inválido!!! Par ou impar? [P/I]: '))

    if total % 2 == 0:
        if parImpar == 'P':
            print(f'O computador jogou {pc} e você jogou {j}, a soma deu PAR!!!')
            print('Você ganhou!!!')
            totwin += 1
        else:
            print(f'O computador jogou {pc} e você jogou {j}, a soma deu PAR!!!')
            print(f'GAME OVER!!! Total de vitórias: {totwin}')
            break
    if total % 2 != 0:
        if parImpar == 'P':
            print(f'O computador jogou {pc} e você jogou {j}, a soma deu IMPAR!!!')
            print(f'GAME OVER!!! Total de vitórias: {totwin}')
            break
        else:
            print(f'O computador jogou {pc} e você jogou {j}, a soma deu IMPAR!!!')
            print('Você ganhou!!!')
            totwin += 1

