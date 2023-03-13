'''Usando a classe Monstro do exercício acima, crie novos tipos de 
monstros Orc, Troll e Vampiro que usam armas e magias específicas.'''


class Monstro:
    def __init__(self, nome, poder, arma):
        self.nome = nome
        self.poder = poder
        self.arma = arma


mago = Monstro("Mago Negro", 2500, "Cajado")

print("O Mago Negro")
print("Nome:", mago.nome)
print("Poder:", mago.poder)
print("Arma:", mago.arma)


class Orc(Monstro):
    def __init__(self, nome, poder, arma):
        super().__init__(nome, poder, arma)


orc = Orc("Xull", 2000, "Canhão")

print("\nXull, O Ogro Chucro")
print("Nome:", orc.nome)
print("Poder:", orc.poder)
print("Arma:", orc.arma)


class Troll(Monstro):
    def __init__(self, nome, poder, arma):
        super().__init__(nome, poder, arma)


troll = Troll("Meme Face", 2600, "O próprio rosto")

print("\nMeme Face, Não é o Sam (South America Memes)")
print("Nome:", troll.nome)
print("Poder:", troll.poder)
print("Arma:", troll.arma)


class Vampiro(Monstro):
    def __init__(self, nome, poder, arma):
        super().__init__(nome, poder, arma)


vampiro = Vampiro("Volkov Carti", 1800, "Foice")

print("\nVolkov Carti, Whole Lotta Red")
print("Nome:", vampiro.nome)
print("Poder:", vampiro.poder)
print("Arma:", vampiro.arma)
