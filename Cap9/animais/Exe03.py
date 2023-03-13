'''Crie uma API para um zoológico. Ela permite listar os animais cadastrados, 
adicionar, editar e remover animais, identificados por um ID único.'''

from fastapi import FastAPI

app = FastAPI()

animais = [
    {
        'id': 1,
        'animal': 'Leão'
    }
]

@app.get("/animais") # indica o endereço que colocaremos na url para que está função seja chamada
def get_animais():
    return animais

#Para testes use http://127.0.0.1:8000/docs
@app.post("/animais")
def criar_animais(nome: str):
    id = len(animais) + 1

    # monta um dicionário com as informações do novo funcionário.
    novo_animal = {
        'id': id,
        'nome': nome
    }

    # adiciona o novo funcionário na lista de funcionários.
    animais.append(novo_animal)

    # retorna os dados do funcionário que foi criado.
    return {'id': id, 'nome': nome}
    
# Para testes use http://127.0.0.1:8000/animais/{animais_id}

@app.put('/animais/{animais_id}')
def atualizar_animais(animal_id: int, animal_atualizado: dict):

    # A lista de funcionários começa na posição 0, o id dos
    # funcionarios inicia no digito 1, sendo assim precisamo
    # subtrair o id informado por 1, para que ele corresponda a
    # posição da lista em que os dados do funcionário está armazenado.
    id = animal_id - 1

    # atualizamos os dados do funcionario com os novos valores que enviamos.
    animais[id] = animal_atualizado

    return animais[id]

@app.delete('/animais/{animais_id}')
def delete_item(animal_id: int):
    id = animal_id - 1

    animal_excluido = animais[id]
    animais[id] = {}

    return animal_excluido 


