'''Escreva um programa que percorra a lista abaixo e 
calcule a divisão de um número informado pelo usuário por cada número. 
Caso não seja possível realizar a divisão, o programa deve imprimir um erro, 
usando tratamento de exceções'''

numeros = [1, 4, 0, 6, 2, 0]
num = float(input("Informe um número:  "))    

for x in numeros:
    try:
        resultado = num / x
            
    except ZeroDivisionError:
        print("O número não deve ser zero")
    else:
        print(resultado)

print("\nFim do programa.")  