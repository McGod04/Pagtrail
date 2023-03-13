'''Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da 
direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. 
Escreva um programa que peça uma string para o usuário e verifique se é um palíndromo.'''

expressao = input("Escreva uma expresão: ").upper().replace(' ', '')
inverter = expressao[::-1]

if expressao == inverter:
    print("É palíndromo, pois, {} invertido é igual a {}.".format(expressao, inverter))
else:
    print("Não é um palíndromo.")
