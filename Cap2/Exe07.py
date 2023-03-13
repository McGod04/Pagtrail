'''Escreva um programa que peça o nome do usuário e em seguida 
mostre o nome de trás para frente e somente em maiúsculas'''

nome = input("Digite o seu nome: ")[::-1]
up = nome.upper()

print(up)