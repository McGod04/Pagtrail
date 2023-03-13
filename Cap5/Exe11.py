'''Complemente a função calcula para aceitar as quatro operações aritméticas básicas: 
adição, subtração, multiplicação e divisão. Caso uma operação não seja informada, retorne a soma.'''

def soma():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("\nSoma: ",x+y)

def subtracao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("\nSubtracao: ",x-y)

def multiplicacao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("\nMultiplicacao: ",x*y)

def divisao():
    x = float(input("Primeiro numero: "))
    y = float(input("Segundo numero: "))
    print("Divisao: ",x/y)

opcao = 1

while opcao:
   print("Escolha uma opção abaixo:\n")
   print("0. Sair")
   print("1. Somar")
   print("2. Subtrair")
   print("3. Multiplicação")
   print("4. Divisão ")

   opcao = int(input("\nOpção: "))

   if(opcao==1):
        soma()
   if(opcao==2):
        subtracao()
   if(opcao==3):
        multiplicacao()
   if(opcao==4):
        divisao()