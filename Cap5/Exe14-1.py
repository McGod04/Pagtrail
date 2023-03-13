'''O que acontece se executarmos o seguintes códigos abaixo e como tratar os erros?

print(name)'''

name = str(input("Digite um nome: "))

try:
    print (name)
except NameError as n:  
    print ("\nNameError: Variável indefinida\n" f"{n}")
else:  
    print ("Successo, sem erros por aqui.") 