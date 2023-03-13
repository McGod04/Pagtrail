'''Escreva um programa que lê as variáveis de ambiente do sistema e 
imprima a variável passada ao executar o programa. 
Variáveis de ambiente podem ser definidas antes do comando da seguinte maneira:

$ MINHA_VARIAVEL=42  python envs.py

A variável é MINHA_VARIAVEL e o valor é 42
'''

import os

os.environ["MINHA_VARIAVEL"] = "42"

var = os.getenv("MINHA_VARIAVEL")

print("A variável é MINHA_VARIAVEL e o valor é", var)