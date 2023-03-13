'''Escreva um programa que copia um arquivo e adiciona o sufixo "teste_" ao nome. Exemplo:

$ python renomeia.py  teste.txt
$ ls
teste.txt  teste_copia.txt
'''

import shutil
import os

basepath = os.path.abspath('.')
origem = os.path.join(basepath, 'teste.txt')
destino = os.path.join(basepath, 'Cap7/')

shutil.copy(origem, destino)

