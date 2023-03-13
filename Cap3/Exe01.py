'''Com base na lista abaixo, crie uma nova lista removendo 
os valores menores que 10: [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]'''

lista = [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]
nova_lista = [x for x in lista if x > 10]
nova_lista.sort()
print(nova_lista)
