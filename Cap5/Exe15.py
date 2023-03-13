'''Complete o código abaixo com as devidas exceções:

print("Aprendendo exceções")
try:
    num1 = int(input("Informe o primeiro número: ")
    num2 = int(input("Informe o segundo número: "))
    quociente = num1 / num2
    print ("Ambos os números foram informados corretamente")
except ________:
    print("Por favor informe apenas números")
except ________:
    print("O segundo número não deve ser zero")
else:
    print(" Great .. you are a good programmer")
__________: # sempre executa no final
    print("Fim do programa")
'''

print("Aprendendo exceções")
try:
    num1 = int(input("\nInforme o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    quociente = num1 / num2
    print ("\nO resultado é" , quociente)
    print ("Ambos os números foram informados corretamente\n")

except ValueError as v:
    print("\nValueError: Por favor informe apenas números\n" f"{v}\n")
except ZeroDivisionError as z:
    print("\nZeroDivisionError: O segundo número não deve ser zero\n" f"{z}\n")
else:
    print("Muito bom. Bom trabalho.")
finally: # sempre executa no final
    print("Fim do programa.")