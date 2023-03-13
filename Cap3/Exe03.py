'''A seguinte lista foi produzida por um processo automático e contém strings vazias indesejadas. 
Crie uma nova lista usando o for-loop que não contenha esses valores.
["Michael", "", "Ana", "Joao", "", "Marcia"]'''

lista_nomes = ["Michael", "", "Ana", "Joao", "", "Marcia"]
nova_lista = list(filter(len, lista_nomes))

print(nova_lista)
