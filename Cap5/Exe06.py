'''Escreva um loop que percorra uma lista de números e retorne apenas os números pares'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

for numero in lista:
    if numero % 2 == 0:
        print(numero, end=" ")