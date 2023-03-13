''' No exemplo abaixo temos uma lista de listas. 
Crie uma nova lista única com todos os nomes
    ["Michael", "Ana", "Joao", "Marcia"],
    ["Fabio", "Luiz", "Lucia", "Malu"],
    ["Jorge", "Maria", "Jose"]'''

nomes = [["Michael", "Ana", "Joao", "Marcia"], [
    "Fabio", "Luiz", "Lucia", "Malu"], ["Jorge", "Maria", "Jose"]]

nova_lista = []

for lista in nomes:
    for nome in lista:

        nova_lista.append(nome)

print(nova_lista)

#nova_lista = [nome for lista in nomes for nome in lista]

'''for lista in nomes:
    nova_lista += lista'''