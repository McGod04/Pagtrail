'''Com base no exercício anterior, converta o módulo lib.py em um pacote lib com alguns novos módulos.
Lembre-se de atualizar os imports!'''

def fib(n):    
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result