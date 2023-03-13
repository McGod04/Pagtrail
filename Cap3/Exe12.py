'''Utilizando o exemplo acima, crie um novo dicionário que inclua os pares do dicionário abaixo:
'''

funcionarios = {
    'mario': {'nome': 'Mario', 'salario': 7500},
    'ana': {'nome': 'Ana', 'salario': 9500},
    'bete': {'nome': 'Elizabeth', 'salario': 6500}
}

novos_funcionarios = {
    'juliana': {'nome': 'Juliana', 'salario': 7000},
    'joao': {'nome': 'João', 'salario': 6200}
}

funcionarios.update(novos_funcionarios)
print(funcionarios)