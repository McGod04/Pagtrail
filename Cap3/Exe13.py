'''Com o dicionário obtido no exercício anterior, escrever um for-loop 
que leia a lista de chaves abaixo e remova os funcionarios Joao e Bete:'''

funcionarios = {
    'mario': {'nome': 'Mario', 'salario': 7500},
    'ana': {'nome': 'Ana', 'salario': 9500},
    'bete': {'nome': 'Elizabeth', 'salario': 6500},
    'juliana': {'nome': 'Juliana', 'salario': 7000},
    'joao': {'nome': 'João', 'salario': 6200}
}

[funcionarios.pop(chave) for chave in ['joao', 'bete']]
print(funcionarios)
