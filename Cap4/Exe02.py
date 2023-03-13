'''Escreva um programa que lê um arquivo e conte quantas linhas o arquivo possui'''

total_artistas = 0

with open('Artistas.txt', encoding="UTF8") as arquivo:

    linhas = arquivo.readlines()

    for row in linhas:
        artistas = row.strip()
        total_artistas += 1

        print(artistas)
print(f"\nO total de artistas é: {total_artistas}")
