'''Acesse o valor 20 na tupla abaixo. Qual a sintaxe necessária?
("red", [10, 20, 30], (5, 15, 25))'''

seq = ("red", [10, 20, 30], (5, 15, 25))
#lista = seq[0]

for x in seq:
    if isinstance(x, list):
        for y in x:
            if y == 20:
                print(y)


# print(seq[1][1])
