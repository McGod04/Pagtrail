'''Escreva um programa que receba três números e retorne qual deles é o maior. 
Se todos forem iguais, retorne que são todos iguais. Exemplo do programa sendo executado:'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))

maior = num1

if num2 > num1 and num2 >= num3:
    maior = num2
    print(f"\nO maior valor digitado foi: {maior}")

elif num3 > num1 and num3 > num2:
    maior = num3
    print(f"\nO maior valor digitado foi: {maior}")

elif num3 >= num1 and num3 >= num2:
    maior = num3
    print(f"\nO maior valor digitado foi: {maior}")

elif num3 == num1 and num3 == num2:
    print("\nTodos são iguais.")

elif num2 == num1 and num2 == num3:
    print("\nTodos são iguais.")

else:
    num2 >= num1 and num2 >= num3
    maior = num2
    print(f"\nO maior valor digitado foi: {maior}")
