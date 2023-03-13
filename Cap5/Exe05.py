'''Calcule a soma dos números de 1 até o número que o usuário informar. 
Por exemplo, se o usuário informar 10, a soma será (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55):'''

soma = 0

n = int(input("Digite um valor: "))

for numero in range(1, n + 1):
    soma += numero

print(f"A soma dos números de 1 até {n} é igual a {soma}\n")
