from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do programa''')
    op = int(input('>>>>> Sua opção: '))

    if op == 1:
        soma = n1 + n2
        print('{} + {} é {:.2f}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1*n2
        print('{} x {} é {:.2f}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior entre {} e {} é {:.2f}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(1)
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')
