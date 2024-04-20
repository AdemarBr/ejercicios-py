'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.'''


def is_vocal(d):
    if (d == "a" or d == "A" or d == "e" or d == "E" or d == "i" or d == "I" or d == "o" or d == "O" or d == "u" or d == "U"):
        return True
    else:
        return False


print(is_vocal("o"))
