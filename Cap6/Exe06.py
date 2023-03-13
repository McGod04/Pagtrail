'''Crie uma classe com um método estático build() 
que construa instâncias de si mesma e conte quantas instâncias foram criadas. Exemplo:

carro1 = Carro.build('Ford')
Total de carros criados: 1

carro2 = Carro.build('Ferrari')
Total de carros criados: 2
'''


class Veículo:

    total = 0

    def __init__(self, marca):
        self.marca = marca
        Veículo.total += 1

    @staticmethod
    def build(marcas):
        Veículo(marcas)
        print("Total de carros criados: ", Veículo.total)


Veículo.build("Ford")
Veículo.build("Fiat")
