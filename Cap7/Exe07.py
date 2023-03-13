'''Crie quatro funções que realizam as operações aritméticas (adição, subtração, multiplicaçao e divisão)
 e escreva testes que verifiquem seus resultados.'''

 # uma função que soma dois números
def soma(a, b):
    return a + b

# um teste da função "soma"
def test_soma():
    assert soma(1, 1) == 2

adicao = soma(1, 1)
print(adicao)

def subtracao(a, b):
    return a - b

# um teste da função "soma"
def test_subtracao():
    assert subtracao(1, 1) == 0

sub = subtracao(1, 1)
print(sub)

def divisao(a, b):
    return a / b

# um teste da função "soma"
def test_divisao():
    assert divisao(2, 2) == 1

div = divisao(1, 1)
print(div)

def mutiplicacao(a, b):
    return a * b

# um teste da função "soma"
def test_multi():
    assert mutiplicacao(5, 5) == 25

mult = mutiplicacao(5, 5)
print(mult)
