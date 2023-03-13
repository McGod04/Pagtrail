from fastapi import FastAPI

app = FastAPI()

funcionarios = [
    {
        'id': 1,
        'nome': 'João',
        'cargo': 'gerente'
    }
]


@app.get("/funcionarios") # indica o endereço que colocaremos na url para que está função seja chamada
def get_funcionarios():
    return funcionarios


#Para testes use http://127.0.0.1:8000/docs
@app.post("/funcionarios")
def criar_funcionarios(nome: str, cargo: str):
    id = len(funcionarios) + 1

    # monta um dicionário com as informações do novo funcionário.
    novo_funcionario = {
        'id': id,
        'nome': nome,
        'cargo': cargo
    }

    # adiciona o novo funcionário na lista de funcionários.
    funcionarios.append(novo_funcionario)

    # retorna os dados do funcionário que foi criado.
    return {'id': id, 'nome': nome, 'cargo': cargo}

# Para testes use http://127.0.0.1:8000/funcionarios/{funcionario_id}

@app.put('/funcionarios/{funcionario_id}')
def atualizar_funcionario(funcionario_id: int, funcionario_atualizado: dict):

    # A lista de funcionários começa na posição 0, o id dos
    # funcionarios inicia no digito 1, sendo assim precisamo
    # subtrair o id informado por 1, para que ele corresponda a
    # posição da lista em que os dados do funcionário está armazenado.
    id = funcionario_id - 1

    # atualizamos os dados do funcionario com os novos valores que enviamos.
    funcionarios[id] = funcionario_atualizado

    return funcionarios[id]

@app.delete('/funcionarios/{funcionario_id}')
def delete_item(funcionario_id: int):
    id = funcionario_id - 1

    funcionario_excluido = funcionarios[id]
    funcionarios[id] = {}

    return funcionario_excluido

