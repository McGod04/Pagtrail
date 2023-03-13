# Timer para o fogão
import time

# enquanto for verdade
while(True):

    # Você tem uma pipoqueira?
    pipoqueira = input("Você tem uma pipoqueira?: ")

    # Se a resposta for diferente de "S"
    if pipoqueira.upper() != "S":

        # Use uma frigideira ou uma panela
        print("Use uma frigideira ou uma panela\n")

    # Senão, vamos fazer pipoca
    else:
        print("Vamos fazer pipoca\n")

    # Você tem milho
    milho = input("Você tem milho?: ")

    # Se não tiver milho
    if milho.upper() != "S":

        # Não tem como fazer pipoca
        print("Não tem como fazer pipoca\n")

        # O código para se a resposta for não
        break

    # Senão, adicione meia xícara de milho na pipoqueira
    else:
        print("Adicionar meia xícara de milho\n")

    # Você tem manteiga?
    manteiga = input("Você tem manteiga?: ")

    # Se a resposta for diferente de "S"
    if manteiga.upper() != "S":

        # Use óleo de soja no lugar da manteiga
        print("Use óleo de soja no lugar da manteiga\n")

    # Senão, adicione uma colher de manteiga na pipoqueira
    else:
        print("Adicionar uma colher de manteiga\n")

    # Você ligou o fogo
    fogão = input("Você ligou o fogo?: ")

    # Se a resposta for "Não"
    if fogão.upper() != "S":

        # Acender o fogo (ps: Cheque se tem gás)
        print("Acender o fogo (ps: Cheque se tem gás)\n")

        # O código para se a resposta for não
        break

    # Senão
    else:
        # Mantenha o fogo baixo
        print("Mantenha o fogo baixo\n")

        # Mexendo a panela...
        print("Mexendo a panela...")

        # Timer de 5 segundos
        time.sleep(5)

        # Desligue o fogo, sua pipoca está pronta!
        print("Desligue o fogo, sua pipoca está pronta!\n")

    # Quer adicionar sal?
    sal = input("Quer adicionar sal?: ")

    # Se a reposta for diferente de "S"
    if sal.upper() != "S":

        # Aproveite a sua pipoca!
        print("Aproveite a sua pipoca!")

        # O código para aqui.
        break

    # Senão, adicione sal a gosto e aproveite sua pipoca!
    else:
        print("Adicione sal a gosto e aproveite sua pipoca!")

        # O código para aqui.
        break
