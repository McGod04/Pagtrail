'''Usando o for loop, gere uma nova lista a partir do 
exemplo acima com todos os números multiplicados por 2.
[2, 120, 30, 174, 26, 18, 16, 62, 84, 4]'''

lista = [2, 120, 30, 174, 26, 18, 16, 62, 84, 4]
nova_lista = []

for x in lista:
    y = x * 2
    nova_lista.append(y)

print(nova_lista)
