'''Reescreva a classe Funcionario do exemplo acima com o atributo promocoes, que armazena 
valores de 1 a 3 que aumentam o salário em uma quantia fixa para cada nível de promoção.'''

class Funcionario:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__salario = 0  

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        return self.__salario == value

ana = Funcionario('Ana', 33)
ana.salario = 1000
print(ana.salario)