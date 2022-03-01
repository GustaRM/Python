lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado! Não foi adicionado...')
    resp = input('Deseja adicionar outro valor? [S/N]: ').upper().strip()
    while True:
        if resp not in 'NS':
            resp = input('Não entendi sua resposta. Deseja adicionar outro valor? [S/N]: ').upper().strip()
        else:
            break
    if resp in 'N':
        break
print('='*30)
print(f'Você digitou os valores {sorted(lista)}')
