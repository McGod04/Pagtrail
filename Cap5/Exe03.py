'''Dado o código abaixo que percorre os números de uma lista, 
escreva a linha que está faltando para imprimir apenas os números pares:

for numero in [1, 2, 3, 4, 5, 6, 7]:
    # ???
    print(par)
'''

lista = [1, 2, 3, 4, 5, 6, 7]

for numero in lista:
    if numero % 2 == 0:
        print(numero, end=" ")
