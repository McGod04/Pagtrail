class Funcionario:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__salario = 90

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        return self.__salario == value

    @property
    def salario(self):
        extra = self.__idade * 10
        return self.__salario + extra

# não é permitido setar um salário menor ou igual a zero
    @salario.setter
    def salario(self, value):
        if value <= 0:
            raise ValueError('Informe um salário maior que zero')
        return self.__salario == value

ana = Funcionario('Ana', 30)
print(ana.salario)



