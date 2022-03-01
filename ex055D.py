from random import randint
from time import sleep

print('-'*30)
print('{:^30}'.format('JOGO MEGA SENA'))
print('-'*30)

j = int(input('Quantos jogos deseja fazer? '))

lista = list()
jogos = list()

tot = 1

while tot <= j:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print()
print('-='*2, f'  \033[32mSORTEANDO {j} JOGOS...\033[m  ', '-='*2)
sleep(1.5)

for i, l in enumerate(jogos):
    print(f'\033[32mJogo {i+1}:\033[m {l}')
    sleep(0.5)
print('-=' * 3, '\033[32m< BOA SORTE! >\033[m', '-=' * 3)
