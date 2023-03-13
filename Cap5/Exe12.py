'''Escreva uma função que recebe nomes e um parâmetro 
opcional de multiplicação que duplica os nomes informados.'''


def mult(num, nome):
    res = num * nome
    return res


def menu():
    num = int(input('\nDigite um número: '))
    nome = input('Digite um nome: ')

    print("\nResultado:", mult(num, nome))


def op():
    while True:

        print("\nDeseja continuar?\n")
        print("1. Sim")
        print("2. Não")

        opcao = int(input("\nOpção: "))

        if(opcao == 1):
            menu()

        if(opcao == 2):
            print("Fim do código")
            break


menu()
op()
