'''Adicione um atributo departamento com um método setter na 
classe Funcionario que aceita apenas valores dentro de uma lista 
['vendas', 'contabilidade', 'marketing'], e dispara uma exceção caso contrário.'''

class Funcionario:
    def __init__(self):
        self._departamento = ['vendas', 'contabilidade', 'marketing']

    @property
    def departamento(self):
        return self._departamento

    @departamento.setter
    def departamento(self, value):
        if value not in self._departamento:
            raise ValueError("Valor não encontrado.")
    
funcionario = Funcionario()
funcionario.departamento = "um"
