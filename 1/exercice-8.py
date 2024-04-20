'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for
anidado. '''
lista1 = [1, 2, 3, 5, 6, 100]
lista2 = [11, 24, 13, 57, 68, 100]


def superposicion(l1, l2):
    for d1 in l1:
        for d2 in l2:
            if (d1 == d2):
                return True
    return False


print(superposicion(lista1, lista2))
