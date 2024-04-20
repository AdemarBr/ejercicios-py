'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''


def es_palindromo(cadena):
    res = ""
    for charr in cadena:
        res = charr + res

    if (cadena == res):
        return True
    else:
        return False


palabra = "radar"

print(es_palindromo(palabra))
