'''Crie uma classe Veículo que armazena e imprima a quantidade de 
veículos criados a cada nova instanciação. Exemplo:

Novo veículo, marca Ford! Total de veículos: 1
Novo veículo, marca Wolkswagen! Total de veículos: 2
Novo veículo, marca Fiat! Total de veículos: 3
Novo veículo, marca Ferrari! Total de veículos: 4'''


class Veículo:

    total = 0

    def __init__(self, marca):
        self.marca = marca

        Veículo.total += 1


carro1 = Veículo("Ford")
print(f"Novo veículo, {carro1.marca}! Total de veículos: {carro1.total}")

carro2 = Veículo("Wolkswagen")
print(f"Novo veículo, {carro2.marca}! Total de veículos: {carro2.total}")

carro3 = Veículo("Fiat")
print(f"Novo veículo, {carro3.marca}! Total de veículos: {carro3.total}")

carro4 = Veículo("Ferrari")
print(f"Novo veículo, {carro4.marca}! Total de veículos: {carro4.total}")
