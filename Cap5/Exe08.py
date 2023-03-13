'''Escreva um programa que use dois for aninhados, ou seja, um loop dentro de outro, que iterem sobre 
uma mesma lista de números e imprima a multiplicação dos números. Por exemplo, dada a lista [1, 2, 3]'''

lista = [1, 2, 3]

for numero1 in lista:
    for numero2 in lista:
        print("%d x %d = %d" % (numero1, numero2, numero1 * numero2))
