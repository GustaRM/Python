lista = ('Lápis', 1,
         'Caneta', 2,
         'Borracha', 0.50,
         'Papel', 20,
         'Estojo', 5,
         'Livro', 40,
         'Compasso', 9.99)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f' R${lista[pos]:>7.2f}')
print('-'*40)
