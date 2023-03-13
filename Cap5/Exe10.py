'''Escreva uma função que recebe um argumento numérico. A função retorna o caractere 'P', 
se seu argumento for positivo, e 'N', se seu argumento for zero ou negativo.'''

def pn(n):
    if n > 0:
        print('Positivo')

    elif n <= 0:
        print('Negativo')

n = int(input('digite um número: '))

print('Este número é', end=' ')
pn(n)