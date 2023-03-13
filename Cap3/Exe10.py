''' Usando os métodos de acesso de dicionários, leia o valor da chave historia no dicionário abaixo:
estudante = {
    "nome": "Maria",
    "notas": {
        "fisica": 70,
        "historia": 80
    }
}'''

estudante = {
    "nome": "Maria",
    "notas": {"fisica": 70, "historia": 80}
}

notas = estudante['notas']
print(notas.get('historia'))
