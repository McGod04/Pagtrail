'''Incremente a classe Monstro com um novo método arma() que devolve a arma que o monstro usa.'''

class Monstro:
    def __init__(self, nome, poder, arma):
        self.nome = nome
        self.poder = poder
        self.arma = arma

mago = Monstro("Mago Negro", 2500, "Cajado")

print(mago.nome)
print(mago.poder)
print(mago.arma)
