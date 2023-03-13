'''Escreva um programa que crie arquivos nomeados com as letras do 
alfabeto (a.txt, b.txt, c.txt), cada um com a letra como seu conteúdo.'''

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H",
            "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for letra in alfabeto:
    with open(f"{letra}.txt", "w") as arquivo:
        arquivo.writelines(letra)


