'''Tuplas são imutáveis, mas listas não. No exemplo abaixo é possível alterar o valor da lista, 
apesar de estar em uma tupla. Isso se deve ao fato de que a tupla guarda a 
referência da lista, não os itens da lista em si. 
Escreva um programa que dobre os valores da lista e 
depois atribua cada um para uma variável diferente.'''

tupla = (11, [22, 33], 44, 55)

primeiro = tupla[1][0] * 2
segundo = tupla[1][1] * 2

print(primeiro, segundo)

#valor1, valor2 = [x * 2 for x in tupla[1]]
#print(valor1, valor2)


#print([x * 2 for x in tupla[1]])
