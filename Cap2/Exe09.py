'''Escreva um programa que exibe o primeiro e o último 
caractere de uma string informada pelo usuário.'''

palavra = input("Escreva uma palavra: ").upper()
primeira_letra = palavra[0]
ultima_letra = palavra[-1]

print("A primeira letra é {} e a ultima é {}.".format(primeira_letra, ultima_letra))