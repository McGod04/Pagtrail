'''Escreva um programa que execute em um loop infinito no qual 
pede que o usuário informe um determinado comando "sair" para interromper o loop. Exemplo: '''

comando = ""

while comando != "sair":

    print("Digite o comando: ")
    comando = input()

    if comando != "sair":
        print("\nErro. Digite novamente.\n")

print("\nFim do código.")
