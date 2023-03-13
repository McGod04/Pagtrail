'''Utilizando o que fizemos até aqui, modifique nosso programa para que opção 
--start seja opcional, de forma que se não for passada a busca será feita no diretório atual.'''

import os
import sys

usage = "\
\nfind.py faz uma busca por caminhos no sistema (arquivos ou diretórios) a partir de um caminho de ponto de partida. \
\n\nModo de uso: \
\n\tfind.py --start [caminho-partida] --name [caminho-busca] \
\n\tfind.py --start [caminho-partida] --type [f|d] \
\nOpções: \
\n\t--start = define o ponto de partida da busca. Obrigatório para utilizar as outras opções\
\n\n\t--name = Procura o valor passado em [caminho-busca] no [caminho-partida] \
\n\t\tExemplo: find.py --start /var/log --name auth.log          -> busca por auth.log dentro do diretório /var/log \
\n\n\t--type = Procura, a partir do [caminho-partida], arquivos se for passado [f] ou diretório se for passado [d] \
\n\t\tExemplo: find.py --start /var/log --type d                 -> busca por todos os diretório dentro de /var/log \
"

print(sys.argv)

if len(sys.argv) == 1:
    print(usage)
    sys.exit()

start = sys.argv[1]


try:
    if start == "--start":
        caminho = sys.argv[1]
        print("O arquivo iniciou com a opção --start")

except IndexError:
    
    if start == "--name":
        caminho = sys.argv[1]
        print("O arquivo iniciou com a opção --name")

    elif start == "--type":
        caminho = sys.argv[1]
        print("O arquivo iniciou com a opção --type")

else:
    caminho = os.path.dirname(os.path.abspath(__file__))

    if start == "--name":
        caminho = sys.argv[2]

    elif start == "--type":
        caminho = sys.argv[2]

print(caminho)
