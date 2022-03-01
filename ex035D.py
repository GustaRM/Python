from random import randint

comp = randint(0, 10)

print('''Sou seu computador
Acabei de pensa em um número de 0 a 10
Tente advinhar!!!''')

p = int(input('Seu palpite: '))
cont = 1

while p != comp:
    if p < 0 or p > 10:
        p = int(input('Tentativa fora do intervalo, tente novamente: '))
        cont += 1
    else:
        if p < comp:
            p = int(input('Mais... Tente outra vez: ' ))
            cont += 1
        else:
            p = int(input('Menos... Tente outra vez: '))
            cont += 1
print('Acertou com {} tentativas. Parabéns!!'.format(cont))
