'''Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.'''


def length(cadena):
    cont = 0
    for charr in cadena:
        cont += 1
    return cont


print(length("briyan mendez"))
