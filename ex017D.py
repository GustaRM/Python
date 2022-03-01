nome = str(input('Digite seu nome: '))

cores = {'limpa': '\033[m',
         'preto': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'verdec': '\033[36m',
         'cinza': '\033[37m'}

limpa = '\033[m'
azul = '\033[34m'
verdec = '\033[36m'

print('Prazer em conhecer você, {}{}{}!'.format(verdec, nome, limpa))
