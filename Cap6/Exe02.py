'''Escreva um programa que defina vários tipos de classes de 
animais e adicione suas instâncias a uma lista. 
Em sequida, percorra a lista chamando um método que retorna o nome dos animais. Exemplo:

Cachorro com nome "Rex"
Gato com nome "Miau"
Papagaio com nome "Paco"
Macaco com nome "Chico"
'''


class Animais:
    def __init__(self, animal, nome):
        self.animal = animal
        self.nome = nome


lista = []
lista.append(Animais("Cachorro", "Rex"))
lista.append(Animais("Gato", "Miau"))
lista.append(Animais("Papagaio", "Paco"))
lista.append(Animais("Macaco", "Chico\n"))

for obj in lista:
    print(obj.animal, "com nome", obj.nome, sep=' ')
