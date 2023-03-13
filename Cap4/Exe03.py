'''Escreva um programa que adiciona um texto arbitrário 
ao final de um arquivo e depois exibe o conteúdo do arquivo.'''

with open('Artistas.txt', 'a', encoding="UTF8") as arquivo:

    arquivo.write("Esses são os artitas deste arquivo.")

with open('Artistas.txt', "r", encoding="UTF8") as arquivo:

    linhas = arquivo.readlines()

    for row in linhas:
        artistas = row.strip()
        print(artistas)
