'''Crie um teste unitário que teste a função abaixo que inverte uma string:

def inverte(texto):
    return texto[::-1]
'''


def inverte(texto):
    return texto[::-1]


def teste_inverte():
    assert inverte("Invertido").upper() == "oditrevni".upper()


msg = inverte("Invertido")
print(msg)
