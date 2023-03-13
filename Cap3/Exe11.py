'''Usando a atribuição de dicionários, atualize o salário da funcionária 
Ana na estrutura abaixo, para o valor 9500:'''

funcionarios = {
    'mario': {'nome': 'Mario', 'salario': 7500},
    'ana': {'nome': 'Ana', 'salario': 8000},
    'bete': {'nome': 'Elizabeth', 'salario': 6500}
}

ana = {'ana': {'nome': 'Ana', 'salario': 9500}}

funcionarios.update(ana)
print(funcionarios)
