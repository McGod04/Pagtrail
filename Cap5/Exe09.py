'''Escreva uma função que recebe vários números e retorna a soma desses números.'''


def soma():
    x = str(input('Digite todos os números: '))
    x = x.strip()
    lista = x.split(" ")
    lista = [int(valor) for valor in lista]
    print("O resultado é:", sum(lista))

def menu():
    while True:

        print("\nDeseja continuar?\n")
        print("1. Sim")
        print("2. Não")

        opcao = int(input("\nOpção: "))

        if(opcao == 1):
            soma()

        if(opcao == 2):
            print("Fim do código")
            break


soma()
menu()
