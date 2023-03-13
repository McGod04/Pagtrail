'''O que acontece se executarmos o seguintes códigos abaixo e como tratar os erros?

import mathes'''

try:
    import mathes 
    print(mathes)

except ModuleNotFoundError as mo:
    print("ModuleNotFoundError: Módulo não importado.\n" f"{mo}")
