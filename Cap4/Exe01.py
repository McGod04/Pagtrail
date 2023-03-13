'''Escreva um programa que lê as dez primeiras linhas de um arquivo.'''

with open('Artistas.txt',"r", encoding="UTF8") as arquivo:

    linhas = arquivo.readlines()[0:10]

    for row in linhas:
        artistas = row.strip()

        print(artistas)
