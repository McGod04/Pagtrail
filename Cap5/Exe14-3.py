'''O que acontece se executarmos o seguintes códigos abaixo e como tratar os erros?

f = open('notfoound.txt', 'r')'''

try:
    f = open('notfoound.txt', 'r', encoding="UTF8")

except FileNotFoundError as f:
    print("FileNotFoundError: Arquivo não existe no diretório.\n" f"{f}")
