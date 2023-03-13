'''Escreva um programa que receba três números e retorne qual deles é o maior. 
Se todos forem iguais, retorne que são todos iguais. Exemplo do programa sendo executado:'''

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

lista = [valor1, valor2, valor3]

if valor1 == valor2 == valor3:
    print("\nTodos os valores são iguais.")

else:
    print('\nO maior numero digitado da lista foi: {} '.format(max(lista)))
