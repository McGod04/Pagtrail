soma = 0

while True:
    
    x = str(input('Digite todos os números: '))
    lista = x.split(",")
    lista = [int(valor) for valor in lista]
    print(sum(lista))

