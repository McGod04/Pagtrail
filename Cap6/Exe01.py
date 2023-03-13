'''Crie uma classe Veículo com os atributos ano e quilometragem. 
Em seguida crie um método que calcule se o veículo precisa ser trocado, isto é, 
se tem mais de 7 anos ou se a quilometragem passou de 100 mil km.'''


class Veículo:
    def __init__(self, ano, km):
        self.ano = ano
        self.km = km


ano = int(input("Qual o ano do seu carro?: "))
km = float(input("Quantos quilometros ele já rodou?: "))

carro = Veículo(ano, km)

if carro.ano < 2015 or carro.km > 100000:
    print("Seu carro precisa ser trocado.\n")

else:
    print("Seu carro está de acordo com os padrões.\n")
